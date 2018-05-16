from flask import Flask
from flask import request

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