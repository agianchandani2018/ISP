from assignment_student_portal import app
from flask import render_template

'''
This will handle rendering the assignment student portal to be displayed in the schoology assignment, pulling in info from GitHub and displaying it.
'''

#returns asp_student.html
def render_student_portal():
	return render_template('asp_student.html', )