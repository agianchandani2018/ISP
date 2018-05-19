**You'll probably want to ignore this -- but this document is for tracking progress, to dos, and general communication or planning.**

---

dropbox submissions? can put all files in dropbox when done

make app for teacher assignment creation

when assignment created, make a Schoology assignment for each student, and embed the link to assignment page in the Schoology assignment

Flask - python/HTML interaction

*the more to do lists i make the emptier i feel inside*

Teacher Assignment Creation
- HTML/javascript

Teacher Form To Do
- [X] Deadline Table
- [ ] Submit info - JSON?
	- [X] add checkpoints list
	- [ ] figure out using jQuery/ajax to send json object to server
- [ ] Disable auto pull requests if not an assignment
- [ ] By default make the last checkpoint the deadline
- [ ] Aid cumulative commit count input
- [ ] Make minimum deadline date = current date
- [ ] Settings for sharing info (TA/instructor github accounts)?
- [ ] After submit, notify if link was invalid

Student Page
- When we embed the html in the schoology assignment, do we want to send a request to the server?

**we may need to make an initial request for github username, add settings later**

Database Attributes
- [ ] assignments
	- [ ] course_sections: sections that have been assigned the assignment
	- [ ] title
	- [ ] sharing permissions: bool
	- [ ] deadline
	- [ ] checkpoints: [{name, date, num commits}]
	- [ ] instructor
- [ ] admin
	- [ ] course_sections: sections that can receive assignments (used in teacher assignment creation)
	- [ ] schoology_id
	- [ ] access_token?
	- [ ] github_username
	- [ ] assignments
	- [ ] github_token?
- [ ] student
	- [ ] schoology_id
	- [ ] access_token?
	- [ ] course_sections
	- [ ] github_username
	- [ ] github_token
	- [ ] assignments: {id: submission_status}



**MAKE GRAPHS**

[Integration Outline Google Doc](https://docs.google.com/document/d/18rlLBixBy4v_k2UCaJfA9dEGO6ejslnkyMPTTGgFZvY/edit)

[Creating Packages in Flask](http://flask.pocoo.org/docs/0.12/patterns/packages/)

[Flask Quickstart](http://flask.pocoo.org/docs/1.0/quickstart/#quickstart)

[requests-oauthlib](https://github.com/requests/requests-oauthlib)

[schoolopy](https://github.com/ErikBoesen/schoolopy)
