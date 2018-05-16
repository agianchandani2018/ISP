from assignment_student_portal import app

'''
This will handle rendering the assignment student portal to be displayed in the schoology assignment, pulling in info from GitHub and displaying it.
'''

@app.route('/')
def index():
	return "Hello World!" #placeholder