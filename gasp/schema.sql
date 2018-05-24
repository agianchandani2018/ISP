DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS assignments;
DROP TABLE IF EXISTS admins;
DROP TABLE IF EXISTS students;


--stores all the assignment info
CREATE TABLE assignments (
	id INT PRIMARY KEY,
	course_sections TEXT, --parse later
	title TEXT,
	sharing_permissions BIT,
	deadline DATETIME,
	checkpoints TEXT,
	instructor INT --id
);

--admins can create courses
CREATE TABLE admins (
	schoology_id VARCHAR(8) PRIMARY KEY,
	schoology_token VARCHAR(100),
	schoology_secret VARCHAR(100),
	course_sections VARCHAR(100),
	github_username VARCHAR(100),
	assignments VARCHAR(100),
	github_token VARCHAR(100)
);

--is it worth making a table for course sections and filtering assignments that way?

--students can access assignments
CREATE TABLE students (
	schoology_id VARCHAR(8) PRIMARY KEY,
	schoology_token VARCHAR(100),
	schoology_secret VARCHAR(100),
	course_sections VARCHAR(100),
	github_username VARCHAR(100),
	github_token VARCHAR(100)
);