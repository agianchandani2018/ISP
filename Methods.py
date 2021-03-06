import requests
import json

class Assignment:

	'''
	Fields:
	username - the owner of the repository
	repoName - the name of the repository to fetch info on
	dec - a json decoder
	repo - the json object of the repo

	**fix later: time zones
	'''

	def __init__(self, username, repoName):
		self.username = username
		self.repoName = repoName
		self.dec = json.JSONDecoder()

		#get the json object for the user info
		self.repo = self.dec.decode(requests.get('https://api.github.com/', auth=(username, '')).text)
		#get the json object for the repository
		self.repo = self.dec.decode(requests.get(self.repo["repository_url"].replace("{owner}", username).replace("{repo}", repoName), "").text)

		#later: error handling?

	#returns a list of all commits with all accompanying information for the repository
	def getCommitList(self):
		c = self.repo["commits_url"].replace("{/sha}", "")
		c = requests.get(c, "")
		return self.dec.decode(c.text)

	def getCommitListMessages(self):
		cL = self.getCommitList()
		list = []
		for e in cL:
			list.append(e["commit"]["message"])
		return list


	#returns the total number of commits for the assignment repo
	def getNumberOfCommits(self):
		return len(self.getCommitList())

	#returns a list containing the dates of each commit
	def getDatesOfCommits(self):
		li = []
		for commit in self.getCommitList():
			li.append(commit["commit"]["committer"]["date"])
		return li

	#returns the number of commits between two given dates
	#form is yyyy-mm-ddThh:mm:ssZ
	#!these times do not line up: probably in different time zone, about 4 hours ahead of actual
	def numCommitsDateRange(self, startDate, endDate):
		c = 0
		for d in self.getDatesOfCommits():
			if(d >= startDate and d <= endDate):
				c += 1
		return c

	#returns a string that indicates if the student is up to date, behind, etc
	def statusMessage(self):
		pass




a = Assignment('agianchandani2018', 'box-exercise-agianchandani2018')
print(a.getDatesOfCommits())
print(a.getNumberOfCommits())
print(a.getCommitListMessages())
#print(a.numCommitsDateRange("2018-05-15T00:00:00Z", "2018-05-16T00:00:00Z"))
