from flask import Flask
from flask import request

import webbrowser as wb

#host student page
#make a package
'''
To Do
- obtain data from form
- create github repos
- create schoology assignment
- when requested, respond with student's asp
- maybe make teacher page??? consider for later
Later
- when requested, modify settings for assignment info
- database interaction for storing checkpoint info?
	- store dict for assignment (assignment_info, assignment/notes, deadline_info, starter_repo_link(for updating root), auto_pull_request)
	- store dict for users (schoology_username, github_username, github_link auth_info?)
- on deadline, auto pull request
'''

app = Flask(__name__)

#import other files
import assignment_student_portal.create_github
import assignment_student_portal.create_schoology
import assignment_student_portal.render_student
import assignment_student_portal.authenticate

#authenticates user upon connection
@app.route('/')
def testAuth():
	with open('assignment_student_portal/schoology_api_keys.txt', 'r') as f:
		cfg = f.readlines()

	DOMAIN = 'https://pingry.schoology.com'
	
	auth = authenticate.Auth(cfg[0][:-1], cfg[1], domain=DOMAIN, three_legged=True)
	url = auth.request_authorization()
	
	if url is not None:
		wb.open(url, new=2)
	
	#we want to replace this eventually
	raw_input('Press enter when ready.')
	
	if not auth.authorize():
		raise SystemExit('account was not authorized.')

	#at this point we have obtained the necessary tokens
	
	#next steps: redirect back to user page
	
	return("it worked!")
	
@app.route('/<user>')
def foo_bar():
	pass
'''
upon authentication:
- open new tab
- close tab
redirect to user page
'''
	
'''
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
	return render_template('asp_student.html', username=username) #for this, pass in dict with user's info
	'''