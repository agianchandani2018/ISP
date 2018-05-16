from assignment_student_portal import app

'''
This will handle creation of a Schoology assignment for the course section.
'''

@app.route('/')
def index():
	return "Hello World!" #placeholder