import json
import logging
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)
@app.route("/")
def index():
    app.logger.info("Someone landed in our page!")
    return "WElCOME!"

@app.route("/students",methods=['GET'])
def display_data():
    app.logger.info("Someone request student data")
    jsonbody = {
        "students" : [],
    }
    with open('data.txt', 'r') as f:
        data = f.read()
        data = data.split('\n')
        for item in data:
            jsonbody["students"].append(item)
        return jsonify(jsonbody)


@app.route("/save/<name>")
def save(name):
    app.logger.info("Someone request wants to save data")
    with open('data.txt', 'a') as f:
        f.write('\n'+name)
        f.close()
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