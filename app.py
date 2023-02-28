import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button1')
def button1():
    # Execute the Python script for button 1 and get the output
    output = subprocess.check_output(['python3', 'script1.py']).decode('utf-8')
    return render_template('output.html', output=output)

@app.route('/button2')
def button2():
    # Execute the Python script for button 2 and get the output
    output = subprocess.check_output(['python3', 'script2.py']).decode('utf-8')
    return render_template('output.html', output=output)

@app.route('/button3')
def button3():
    # Execute the Python script for button 3 and get the output
    output = subprocess.check_output(['python3', 'script3.py']).decode('utf-8')
    return render_template('output.html', output=output)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
