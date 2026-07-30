 # Flask Application Source Code (app.py)
from flask import Flask, render_template, request, redirect, url_for, session from werkzeug.security import check_password_hash from functools import wraps import csv from datetime import datetime import os
app = Flask(name) app.secret_key = "super_secret_key"
USERS_FILE = 'users.csv' 
ICS_FILE = 'icsdata.csv' 
ACCESS_LOG = 'access_log.csv' 
AUDIT_LOG = 'audit_log.csv' 
CLOUD_FILE = 'cloud.html'

# LOGGING (AU-2)
----------------------------
@app.before_request 
def log_request(): 
# Create file with header if it doesn't exist 
if not os.path.exists(ACCESS_LOG): 
with open(ACCESS_LOG, 'w') as f: f.write("timestamp,ip,method,path\n")
# Append log entry
with open(ACCESS_LOG, 'a') as f:
    f.write(f"{datetime.now()},{request.remote_addr},{request.method},	  	 	 {request.path}\n")
 
def log_admin_action(user, action, target): 
# Create file with header if it doesn't exist 
if not os.path.exists(AUDIT_LOG): 
with open(AUDIT_LOG, 'w') as f: f.write("timestamp,user,action,target\n")
# Append log entry
	with open(AUDIT_LOG, 'a') as f:
   		 f.write(f"{datetime.now()},{user},{action},{target}\n")
 
# AUTH HELPERS
----------------------------
def get_users(): 
with open(USERS_FILE, 'r') as file: 
return list(csv.DictReader(file))

def save_users(users, fieldnames): 
with open(USERS_FILE, 'w', newline='') as file: 
writer = csv.DictWriter(file, fieldnames=fieldnames) writer.writeheader() 		 	writer.writerows(users)

def update_last_login(username): 
users = get_users() fieldnames = users[0].keys()
for user in users:
    		if user['username'] == username:
       		 user['last_login'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

save_users(users, fieldnames)
 
# DECORATORS
----------------------------
def login_required(f): 
@wraps(f)
 def wrapper(*args, **kwargs): 
if 'username' not in session: 
return redirect(url_for('login')) 
return f(*args, **kwargs) 
return wrapper

def admin_required(f): 
@wraps(f) 
def wrapper(*args, **kwargs): 
if session.get('role') != 'admin': return "Access denied", 403 
return f(*args, **kwargs) 
return wrapper

# LOGIN (AC-7 LOCKOUT)
----------------------------
@app.route('/', methods=['GET', 'POST']) 
def login(): error = None
if request.method == 'POST':
   	 username = request.form['username']
   	 password = request.form['password']

    	users = get_users()
    	fieldnames = users[0].keys()

   	 for user in users:
       	 if user['username'] == username:

            	# Check if locked
        	 if user['locked'] == 'True':
                error = "Account locked. Contact admin."
                return render_template('login.html', error=error)

            # Correct password
            if check_password_hash(user['password'], password):
                user['failed_attempts'] = '0'
                session['username'] = username
                session['role'] = user['role']
                update_last_login(username)
                save_users(users, fieldnames)

                return redirect(url_for('index'))

            # Wrong password
            else:
                attempts = user.get('failed_attempts', '0')

                # Handle empty or invalid values
                if not attempts.isdigit():
                    attempts = '0'

                user['failed_attempts'] = str(int(attempts) + 1)

                # Lock account after 4 attempts
                if int(user['failed_attempts']) >= 4:
                    user['locked'] = 'True'
                    log_admin_action(username, "ACCOUNT_LOCKED", "self")
                    error = "Account locked after too many failed attempts."
                else:
                    error = "Invalid credentials."

                save_users(users, fieldnames)
                return render_template('login.html', error=error)

    # If username not found
    error = "User not found."

return render_template('login.html', error=error)
 
LOGOUT
----------------------------
@app.route('/logout') 
@login_required 
def logout(): session.clear() 
return redirect(url_for('login'))

HOME (AC-9)
----------------------------
@app.route('/myapp') 
@login_required 
def index(): 
users = get_users() last_login = ""
for user in users:
    	if user['username'] == session['username']:
       	 last_login = user.get('last_login', "")

	return render_template('index.html',
                       username=session['username'],
                       last_login=last_login)
 
THE ABOUT PAGE
----------------------------
@app.route('/About')
 @login_required 
def myabout(): 
return render_template('about.html')
 
VIEW ICS DATA
----------------------------
@app.route('/ICS') 
@login_required  
def icsdata(): 
with open(ICS_FILE, 'r') as file: reader = csv.DictReader(file) data = list(reader)
return render_template('ics.html', data=data)
 
VIEW CLOUD INFO
----------------------------
@app.route('/cloud')
 @login_required 
def cservices():
return render_template('cloud.html')
 
ADMIN: MANAGE SENSOR DATA
----------------------------
@app.route('/manage_ics', methods=['GET', 'POST']) 
@admin_required 
def manage_ics(): 
with open(ICS_FILE, 'r') as file: reader = csv.DictReader(file) fieldnames = reader.fieldnames data = 	list(reader)
if request.method == 'POST':
   	 action = request.form.get('action')

   	 if action == 'insert':
       	 new_row = {
            'Time': request.form['Time'],
            'Temperature': request.form['Temperature'],
            'Humidity': request.form['Humidity']
        }
        data.append(new_row)
        log_admin_action(session['username'], "INSERT", new_row['Time'])

    elif action == 'update':
        for row in data:
            if row['Time'] == request.form['Time']:
                row['Temperature'] = request.form['Temperature']
                row['Humidity'] = request.form['Humidity']
                log_admin_action(session['username'], "UPDATE", row['Time'])

    elif action == 'delete':
        time_val = request.form['Time']
        data = [row for row in data if row['Time'] != time_val]
        log_admin_action(session['username'], "DELETE", time_val)

    with open(ICS_FILE, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

return render_template('manage_ics.html', data=data)
 
VIEW ACCESS LOGS (ADMIN ONLY)
----------------------------
@app.route('/access_logs') 
@admin_required 
def view_access_logs(): 
logs = []
# Create file if missing
	if not os.path.exists(ACCESS_LOG):
   	 with open(ACCESS_LOG, 'w') as f:
      	  f.write("timestamp,ip,method,path\n")

# Read logs
	with open(ACCESS_LOG, 'r') as file:
   	 reader = csv.DictReader(file)
   	 logs = list(reader)

# Show newest first
	logs.reverse()

return render_template('access_logs.html', logs=logs)
 
ADMIN: UNLOCK USERS
----------------------------
@app.route('/manage_users', methods=['GET', 'POST'])
 @admin_required 
def manage_users(): 
users = get_users() fieldnames = users[0].keys()
if request.method == 'POST':
   	 username = request.form['username']

    	for user in users:
       	 if user['username'] == username:
          	  user['locked'] = 'False'
            	user['failed_attempts'] = '0'
            log_admin_action(session['username'], "UNLOCK_ACCOUNT", username)

    save_users(users, fieldnames)

return render_template('manage_users.html', users=users)
 
RUN
----------------------------
if name == 'main': app.run(debug=True)

Include:
Login system
Logging functions
Admin routes
Lockout logic

