from flask import Flask
from flask import request

#host student page
#make a package

app = Flask(__name__)

@app.route('/student/<username>')
def show_assigment_portal(username):
	return "portal created for %" % username
	
#use methods argument of route() to handle different HTTP methods
@app.route('/auth', methods=['GET', 'POST'])
def auth():
	if request.method == 'POST': #
		return some_method()
	else:
		return some_other_method()
	
@app.route('/student/<username>')
def render_asp(username=None):
	return render_template('something.html', username=username)