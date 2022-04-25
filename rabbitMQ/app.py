import json
import mysql.connector
import logging
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)
def save_to_db(name, program):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Mine963258741",
        database="testdb",
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO students (name, program) VALUES (%s, %s)"
    val = (name, program)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    mydb.close()

# def get_from_db():
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         passwd="Mine963258741",
#         database="testdb",
#     )
#     mycursor = mydb.cursor()
#     mycursor.execute("SELECT * FROM students")
#     myresult = mycursor.fetchall()
#     mycursor.close()
#     mydb.close()
#     students = []
#     for row in myresult:
#         students.append(row[0])
#     jsonbody = {
#         "products" : students,
#     }
#     return jsonify(jsonbody)

@app.route("/")
def index():
    app.logger.info("Someone landed in our page!")
    return "WElCOME!"

@app.route("/students",methods=['GET'])
def display_data():
    app.logger.info("Someone request student data")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Mine963258741",
        database="testdb",
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM students")
    myresult = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    students = []
    for row in myresult:
        students.append(row[0])
    jsonbody = {
        "students" : students,
    }
    return jsonify(jsonbody)

@app.route("/save/<name>")
def save(name):
    app.logger.info("Someone request wants to save data")
    save_to_db(name, "Software Engineering")
    jsonbody = {
        "student" : name,
    }
    return jsonify(jsonbody)

@app.after_request
def log_the_status_code(response):
    status_as_string = response.status
    logging.warning("status %s" % status_as_string)
    return response

if __name__ == '__main__':
    app.run(port=8080,debug=True)