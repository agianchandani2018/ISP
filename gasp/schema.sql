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
	schoology_id TEXT PRIMARY KEY,
	schoology_token TEXT,
	schoology_secret TEXT,
	course_sections TEXT,
	github_username TEXT,
	assignments TEXT,
	github_token TEXT
);

--is it worth making a table for course sections and filtering assignments that way?

--students can access assignments
CREATE TABLE students (
	schoology_id TEXT PRIMARY KEY,
	schoology_token TEXT,
	schoology_secret TEXT,
	course_sections TEXT,
	github_username TEXT,
	github_token TEXT
);