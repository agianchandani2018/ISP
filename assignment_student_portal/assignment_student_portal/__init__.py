from flask import Flask, request, redirect, url_for, render_template, session

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
import assignment_student_portal.create_github #clone repo on creation
import assignment_student_portal.create_schoology #create assignment on creation
import assignment_student_portal.render_student #pull info for rendering
import assignment_student_portal.authenticate #schoolopy auth
import assignment_student_portal.main #schoolopy api

auth = None #make globally accessible Auth instance

#authenticates user upon connection
@app.route('/')
def index():
	with open('assignment_student_portal/schoology_api_keys.txt', 'r') as f:
		cfg = f.readlines()

	#DOMAIN = 'https://pingry.schoology.com'
	DOMAIN = url_for('finish_auth', _external=True)#app.route
	
	global auth
	auth = authenticate.Auth(cfg[0][:-1], cfg[1], domain=DOMAIN, three_legged=True)
	url = auth.request_authorization()
	
	if url is not None:
		wb.open(url, new=0)
	
	#we want to replace this eventually
	#raw_input('Press enter when ready.')
	
	#if not auth.authorize():
		#raise SystemExit('account was not authorized.')

	#at this point we have obtained the necessary tokens
	
	#next steps: redirect back to user page
	#return redirect(url_for(userpage))
	
	return("it worked!")
	
@app.route('/auth')
def finish_auth():
	global auth
	if not auth.authorize(): 
		raise SystemExit('account was not authorized.')
	
	print main.Schoology(auth).get_me().uid
	return "success"
	
@app.route('/<user>')
def user_status_check(user):
	#if user is admin
		#return render_admin_portal()
	#else
		#return render_student.render_student_portal()
	pass
	
@app.route('/<user>/create', methods=['GET', 'POST'])
def create_assignment(user):
	if request.method == 'POST':
		#run all the stuff to create assignment
		#attempt to access github repo, clone repo, and make assignments
		#make comprehensive error message here
		#if create_github. == None:
			#return ""
		#create schoology assignment
		#create_schoology.
		return "Form submitted successfully."
	else: #request.method == 'GET'
		return render_template('create_assignment.html') #later: add default fill info
	

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
		return put_in_db_i_guess()
	elif request.method == 'GET':
		return render_asp() #or something
	else:
		return some_other_method()
	
@app.route('/student/<username>')
def render_asp(username=None):
	return render_template('asp_student.html', username=username) #for this, pass in dict with user's info
	'''