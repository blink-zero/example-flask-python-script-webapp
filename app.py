from flask import Flask, render_template, redirect, request, session, url_for
import subprocess

app = Flask(__name__)
app.secret_key = 'my_secret_key'

# Define the valid user IDs and passwords
valid_users = {'admin': 'password123', 'user1': 'password456', 'user2': 'password789'}

# Define the login route
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']
        if user_id not in valid_users:
            error = 'Invalid user ID'
        elif password != valid_users[user_id]:
            error = 'Invalid password'
        else:
            session['user_id'] = user_id
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

# Define the home route
@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('home.html', user_id=session['user_id'])

# Define the button1 route
@app.route('/button1')
def button1():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    # Run the button1 script here
    output = subprocess.check_output(['python3', 'script1.py'])
    return render_template('output.html', output=output.decode())

# Define the button2 route
@app.route('/button2')
def button2():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    # Run the button2 script here
    output = subprocess.check_output(['python3', 'script2.py'])
    return render_template('output.html', output=output.decode())

# Define the button3 route
@app.route('/button3')
def button3():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    # Run the button3 script here
    output = subprocess.check_output(['python3', 'script3.py'])
    return render_template('output.html', output=output.decode())
# Define the logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
