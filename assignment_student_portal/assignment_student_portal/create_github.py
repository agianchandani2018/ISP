from assignment_student_portal import app

'''
This will handle everything regarding creation of GitHub repositories for each student.
'''

@app.route('/')
def index():
	return "Hello World!" #placeholder