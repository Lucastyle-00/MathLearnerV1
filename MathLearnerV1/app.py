from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('MathLearner.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    classes = conn.execute('SELECT * FROM class').fetchall()
    conn.close()
    return render_template('index.html', classes=classes)

@app.route('/classlist/<classid>')
def classlist(classid):
    conn = get_db_connection()
    classinfo = conn.execute('SELECT * FROM class WHERE ClassID = ?',(classid,)).fetchone()
    students = conn.execute('SELECT * FROM progress, student WHERE progress.StudentID=student.StudentID AND progress.ClassID = ?',(classid,)).fetchall()
    teacher = conn.execute('SELECT * FROM teacher, class WHERE teacher.TeacherID=class.TeacherID AND ClassID = ?',(classid,)).fetchone()
    conn.close()
    return render_template('class.html', classinfo=classinfo, students=students, teacher=teacher)

@app.route('/teacher/<teacherid>')
def teacher(teacherid):
    conn = get_db_connection()
    teacherinfo = conn.execute('SELECT * FROM teacher WHERE TeacherID = ?',(teacherid,)).fetchone()
    classes = conn.execute('SELECT * FROM class WHERE class.TeacherID = ?',(teacherid,)).fetchall()
    conn.close()
    return render_template('teacher.html', teacherinfo=teacherinfo, classes=classes)

@app.route('/student/<studentid>')
def student(studentid):
    conn = get_db_connection()
    studentinfo = conn.execute('SELECT * FROM student WHERE StudentID = ?',(studentid,)).fetchone()
    classes = conn.execute('SELECT * FROM class, progress WHERE class.ClassID=progress.ClassID AND progress.StudentID = ?',(studentid,)).fetchall()
    conn.close()
    return render_template('student.html', studentinfo=studentinfo, classes=classes)

if __name__ == '__main__':
    app.run(debug=True)
