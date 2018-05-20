from assignment_student_portal import app
from flask import render_template

'''
This will handle rendering the admin portal to be displayed in the schoology app, giving the option to view, create, or edit assignments, linking to the create_assignment page and pulling in info from GitHub and the database as necessary and displaying it.
'''

#renders asp_admin.html
def render_admin_index(schoology):
	'''
	Pass in parameters:
	- schoology object
	- 
	'''
	pass

#redirect to separate pages somewhere in here?



#renders overview of the assignment for all students
@app.route("/<user>/<assignment_id>")
def admin_assignment_overview(user, assignment_id):
	#in the html page, have a dropdown select for all the students
	pass

#renders the assignment page for the selected student
@app.route("/<user>/<assignment_id>/<student>")
def admin_view_individual(user, assignment_id, student):
	#basically just the student assignment
	pass
