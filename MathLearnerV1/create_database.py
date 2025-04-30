#This python script creates a database and populates it with tables.
#If the tables already exist, they are dropped and re-created.

import sqlite3

connection = sqlite3.connect('MathLearner.db')
connection.row_factory = sqlite3.Row

query = 'DROP TABLE If EXISTS Student;'
result = connection.execute(query)

query = 'CREATE TABLE Student (StudentID INTEGER PRIMARY KEY,StudentName varchar(255),Score int,GroupID int);'
result = connection.execute(query)

query = "INSERT INTO Student (StudentName,Score,GroupID) VALUES ('test1',555,1);"
result = connection.execute(query)

query = "INSERT INTO Student (StudentName,Score,GroupID) VALUES ('test2',555,3);"
result = connection.execute(query)

query = "INSERT INTO Student (StudentName,Score,GroupID) VALUES ('test3',555,1);"
result = connection.execute(query)

connection.commit()

query = 'DROP TABLE If EXISTS Teacher;'
result = connection.execute(query)

query = 'CREATE TABLE Teacher (TeacherID INTEGER PRIMARY KEY, Courses_Created int, StatusRole varchar(255), TeacherName varchar(255));'
result = connection.execute(query)

query = "INSERT INTO Teacher (Courses_Created,StatusRole,TeacherName) VALUES (25,'Tutor','Martin');"
result = connection.execute(query)

query = "INSERT INTO Teacher (Courses_Created,StatusRole,TeacherName) VALUES (18,'Head Tutor','Molly');"
result = connection.execute(query)

query = "INSERT INTO Teacher (Courses_Created,StatusRole,TeacherName) VALUES (1,'Assistant Tutor','Martin');"
result = connection.execute(query)

connection.commit()


query = 'DROP TABLE If EXISTS Class;'
result = connection.execute(query)

query = 'CREATE TABLE Class (ClassID INTEGER PRIMARY KEY,TeacherID int,ClassName varchar(255));'
result = connection.execute(query)

query = "INSERT INTO Class (TeacherID,ClassName) VALUES (2,'Geometric Engineers');"
result = connection.execute(query)

query = "INSERT INTO Class (TeacherID,ClassName) VALUES (1,'Alega Bros');"
result = connection.execute(query)

query = "INSERT INTO Class (TeacherID,ClassName) VALUES (2,'Linear Gaming Graphics');"
result = connection.execute(query)

connection.commit()


query = 'DROP TABLE If EXISTS Progress;'
result = connection.execute(query)

query = 'CREATE TABLE Progress (StudentID int,ClassID int,PercentComplete int,Comment varchar(255));'
result = connection.execute(query)

query = "INSERT INTO Progress (StudentID,ClassID,PercentComplete,Comment) VALUES (3,1,23,'Great');"
result = connection.execute(query)

query = "INSERT INTO Progress (StudentID,ClassID,PercentComplete,Comment) VALUES (3,2,13,'Good start');"
result = connection.execute(query)

query = "INSERT INTO Progress (StudentID,ClassID,PercentComplete,Comment) VALUES (1,2,38,'Almost there');"
result = connection.execute(query)

query = "INSERT INTO Progress (StudentID,ClassID,PercentComplete,Comment) VALUES (1,3,29,'Needs more time');"
result = connection.execute(query)

query = "INSERT INTO Progress (StudentID,ClassID,PercentComplete,Comment) VALUES (2,2,14,'Getting there');"
result = connection.execute(query)


connection.commit()
