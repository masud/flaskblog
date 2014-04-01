#!/usr/bin/env python3
from flask import *
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html', page_title='First Page')

@app.route('/contact', methods=['GET','POST'])
def contact() :
	error = None
	if request.method == 'POST' :
		pass
		# @ToDo Some Works
	return render_template('contact.html')	

@app.route('/login', methods=['GET','POST'])
def login():
	error = None
	if(request.method == 'POST'):
		if request.form['username'] != 'admin' or request.form['password'] != 'admin' :
			error = 'Invalid Credential!'
		else :
			return redirect( url_for('home'))
	return render_template('login.html', error = error)

app.debug = True
if __name__ == '__main__' :
	app.run()

			

