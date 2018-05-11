import requests
import json

class Assignment:
	
	def __init__(self, username, repoName):
		self.username = username
		self.repoName = repoName
	
	#returns the total number of commits for the assignment repo
	def getNumberOfCommits(self):

	#returns a list containing the dates of each commit
	def getDatesOfCommits(self):

	#returns the number of commits between two given dates
	def numCommitsDateRange(self, startDate, endDate):

	# returns a string that indicates if the student is up to date, behind, etc
	def statusMessage(self):
