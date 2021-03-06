import os
from flask import Flask, request, redirect, url_for, render_template, session, g
from sqlite3 import dbapi2 as sqlite3
from flask_github import GitHub


import webbrowser as wb

#host student page
#make a package
'''
To Do
- obtain data from form
- create github repos
- create schoology assignment
- when requested, respond with student's asp
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
import assignment_student_portal.render_admin #handle admin portal rendering
import assignment_student_portal.authenticate #schoolopy auth
import assignment_student_portal.main #schoolopy api

#database stuff

app.config.update(dict(
	DATABASE=os.path.join(app.root_path, 'assignment_student_portal.db'),
	DEBUG=True,
	#SECRET_KEY='development key',
	#USERNAME='admin',
	#PASSWORD='default'
))
app.config.from_envvar('ASP_SETTINGS', silent=True)

#connects to the specific database
def connect_db():
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv
	
#initializes the database
def init_db():
	db = get_db()
	with app.open_resource('schema.sql', mode='r') as f:
		db.cursor().executescript(f.read())
	db.commit()

#creates the database tables
@app.cli.command('initdb')
def initdb_command():
	init_db()
	print('initialized the database.')
	
#opens new database connection if there is none yet for current application context
def get_db():
	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db
	
#closes database again at thee end of the request
@app.teardown_appcontext
def close_db(error):
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()

		
# GitHub Stuff
app.config['GITHUB_CLIENT_ID'] = 'placeholder' #placeholders
app.config['GITHUB_CLIENT_SECRET'] = 'yyy'

github = GitHub(app)



auth = None #make globally accessible Auth instance

#authenticates user upon connection
@app.route('/')
def index():
	git_auth()
	db = get_db()
	
	#db.execute('select ')
	#db.commit()
	
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
	
	'''
	db = get_db()
	db.execute('insert into users (id, username, password) values (125, "ja", "pass")')
	db.commit()
	cur = db.execute('select * from users')
	print cur.fetchall()
	'''
	
	
	return("it worked!")
	
#authorizes the user and redirects to the given url
@app.route('/test')
def git_auth():
	return github.authorize(scope="repo", redirect_uri=url_for("finish_auth", _external=True))

@app.route('/github-callback')
@github.authorized_handler
def authorized(oauth_token):
	next_url = request.args.get('next') or url_for('index')
	if oauth_token is None:
		flash("authorization failed.")
		return redirect(next_url)
	user = User.query.filter_by(github_access_token=oauth_token).first()
	if user is None:
		user = User(oauth_token)
		db_session.add(user)
	user.github_access_token = oauth_token
	db_session.commit()
	return redirect(next_url)

@github.access_token_getter
def token_getter():
	user = g.user
	if user is not None:
		return user.github_access_token
	
	
@app.route('/auth')
def finish_auth():
	global auth
	if not auth.authorize(): 
		raise SystemExit('account was not authorized.')
	
	return redirect(url_for('user_status_check', user=main.Schoology(auth).get_me().uid))
	#at some point we need to store access tokens
	
	
@app.route('/<user>')
def user_status_check(user):
	#check if user has the necessary tokens for github access
	
	#if user is admin
		#return render_admin_portal()
	#else
	return render_student.render_student_portal(main.Schoology(auth))
	#return "made it to " + user
	
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
		#render a button to return to home page
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