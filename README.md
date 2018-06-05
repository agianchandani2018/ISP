To run assignment_student_portal package in Windows CMD:
```
set FLASK_APP=assignment_student_portal/__init__.py
flask run
```
To reinitialize the database:
```
flask initdb
```

This project now runs on the Pingry compsci-dev server at http://compsci-dev.pingry.k12.nj.us.1030


This project uses components of the [schoolopy](https://github.com/ErikBoesen/schoolopy) Python wrapper for the Schoology REST API.


# Future Implementation
Due to time constraints, unforeseen setbacks, and the unprecedented amount of time required to learn how to incorporate numerous different languages into this project, it is unlikely that we will be able to complete this project in time for the ISP presentations. Therefore, I will outline the general idea of what this project was supposed to entail, so that compsci students in the future may work to complete this project if they so desire.

## Language Details
This project primarily uses Flask (python) for the server, sqlite3 for storing user information in a database, jinja2 for templates so python can render HTML pages, and javascript/CSS for styling forms.

## Project Overview
The **GASP** (GitHub Assignment Student Portal) is an integration of GitHub into Schoology for the purpose of streamlining the process of creating repositories containing starter code for computer science assignments on GitHub and coordinating corresponding Schoology assignments to notify students of suggested deadlines. It is designed not only to make it easier for instructors to distribute and collect assignments, but also to make it more convenient for students to view their progress on the assignment.

## Features
When an instructor creates an assignment, they must provide the basic information for the assignment as well as a link to the public starter repo on GitHub. The form for assignment creation allows the instructor to customize the assignment, with options for making "checkpoints" of a specified number of commits by a certain date and even for making auto pull-requests on the assignment's due date, regardless of whether or not a student has submitted the assignment.
Once the instructor submits the assignment creation form, the GASP clones the GitHub repository for each student, giving sharing permissions to the instructor and any TAs. It also creates a corresponding Schoology assignment in the course section.
When the student goes to view their assignment on Schoology, it will display the summary statistics for the assignment, including their progress towards the given commit deadlines, an indication of changes in the starter repo, and an option to submit the assignment.
When the teacher views the app on Schoology, they will be directed to an index page, which gives options to either create a new assignment, edit an existing assignment, or view student progress on current assignments. Ideally, the teacher would be able to see a dropdown menu of their courses and select the assignment they wish to view. The app would display an overview of the class's progress towards the commit deadline, as well as an option to view each individual student's progress (displaying a page much like the student's personal assignment portal).


## Next Steps
This project has a lot of potential, but unfortunately it was too much to complete in less than a month. These are future steps that can be taken to create an effective classroom tool for future computer science students.
- [X] Schoology Authentication
	- Schoology authentication is required so that the app can access the student's data. For instructors, permission is required to create assignments and view info such as course sections, etc.
- [X] GitHub Authorization
	- GitHub authorization is required to retrieve a summary of the user's progress in private repos.
- [ ] Database
	- Some information, such as a user's assignments, course sections, and access tokens are stored in the database.
- [ ] Clone GitHub Repository
- [ ] Create Schoology Assignment
- [ ] Render Assignment Student Portal
	- Pull information from the GitHub repository and display it.
- [ ] Render Admin Assignment Portal
	- Display a summary of each student's progress.

## Resources
[GitHub Classroom](https://github.com/education/classroom) as an example for cloning repositories
[schoolopy](https://github.com/ErikBoesen/schoolopy) Python wrapper for the Schoology API

