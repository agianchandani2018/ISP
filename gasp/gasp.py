import os
from flask import Flask, request, redirect, url_for, render_template, session, g, flash
from sqlite3 import dbapi2 as sqlite3
from flask_github import GitHub

import webbrowser as wb


# help


app = Flask(__name__)

import authenticate, main

#----------database stuff----------

app.config.update(dict(
	DATABASE=os.path.join(app.root_path, 'gasp.db'),
	DEBUG=True,
	#SECRET_KEY='development key',
	#USERNAME='admin',
	#PASSWORD='default'
))
app.config.from_envvar('GASP_SETTINGS', silent=True)

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

		
#----------GitHub Stuff----------
app.config['GITHUB_CLIENT_ID'] = 'placeholder' #placeholders
app.config['GITHUB_CLIENT_SECRET'] = 'yyy'

github = GitHub(app)


auth = None #make globally accessible Auth instance


#----------View Functions----------

#authenticates user upon connection
@app.route('/')
def index():
	#git_auth()
	db = get_db()
	
	#db.execute('select ')
	#db.commit()
	
	#with open('assignment_student_portal/schoology_api_keys.txt', 'r') as f:
		#cfg = f.readlines()
	cfg = [raw_input("key") + " ", raw_input("secret")]
	
	print(cfg)

	DOMAIN = url_for('finish_auth', _external=True)#app.route
	
	global auth
	auth = authenticate.Auth(cfg[0][:-1], cfg[1], domain=DOMAIN, three_legged=True)
	url = auth.request_authorization()
	
	if url is not None:
		#wb.open(url, new=0, autoraise=True)
		#return "successful url " + url
		return redirect(url)
	
	return("bad url " + url)
	
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
	db = get_db()
	
	ids = db.execute('select schoology_id from admins').fetchall()
	
	if str(user) in ids:
		return "reached admin page for " + user
	else:
		return "probably a student " + user
	
	
	#if user is admin
		#return render_admin_portal()
	#else
	#return render_student.render_student_portal(main.Schoology(auth))
	#return "made it to user " + user
	
@app.route('/add/<user>')
def test_add_admin(user):
	db = get_db()
	print(type(user))
	db.execute('insert into admins (schoology_id) values ?', user)
	db.commit()
	return 'added a new admin ' + user
	
@app.route('/addu/<user>')
def test_add_user(user):
	db = get_db()
	db.execute('insert into students (schoology_id) select ?', user)
	db.commit()
	return "added a new student " + user
	
@app.route('/<user>/create', methods=['GET', 'POST'])
def create_assignment(user):
	if request.method == 'POST':
		#run all the stuff to create assignment
		#attempt to access github repo, clone repo, and make assignments
		#make comprehensive error message here
		#if create_github. == None:
			#return ""
		#create schoology assignment
		
		#add assignment to database
		
		flash("Form submitted successfully.")
		return redirect(url_for('user_status_check', user=user))

	else: #request.method == 'GET'
		return render_template('create_assignment.html', course_list=["per1", "per2"]) #later: add default fill info
	
@app.route('/hidden/initdb') #can't find a better way to do this
def initialize_database():
	init_db()
	return "success!"
	
@app.route('/hidden/dbcontents')
def spill_db_contents():
	return "replace with db contents"
	
if __name__=='__main__':
	app.run(debug=True,host="compsci-dev.pingry.k12.nj.us", port=1030)
#filezilla ssh protocol