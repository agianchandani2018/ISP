from assignment_student_portal import app
from flask import render_template

'''
This will handle rendering the assignment student portal to be displayed in the schoology assignment, pulling in info from GitHub and displaying it.
'''

#takes in an instance of the Schoology class and renders the student portal
def render_student_portal(schoology):
	'''
	vars to pass in:
	- schoology assignment id (https://pingry.schoology.com/assignment/1489067395/info)
	- assignment_name
	- current_date
	'''
	return render_template('asp_student.html', assignment_name="Assignment 1", checkpoints=checkpoint_status(), current_date="20180103")

#fetch data from github and return a list of dicts representing checkpoints 
#{name: "", date: "", commit_goal: #, commits: #}
def checkpoint_status():
	return[{'name':"start", 'date': "20180101", 'commit_goal': 3, 'commits': 2}, {'name':"mid", 'date': "20180102", 'commit_goal': 3, 'commits': 5}, {'name':"end", 'date': "20180105", 'commit_goal': 7, 'commits': 5}] #placeholder
	
#returns a string telling if a student has submitted their assignment yet
def submission_status():
	pass
	#should be in student's database info
	
#returns a message if there have been any updates to the root directory
#and the date of that last update
def starter_updates():
	pass
	
#this may already be implemented so check somewhere first
#returns the current date
def get_current_date():
	pass
	
#low priority but hey those style points :D
def graphs():
	pass
	
#anything else that we should add for student portal?
