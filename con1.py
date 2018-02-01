from flask import Flask,render_template
import pymongo
from flask_pymongo import PyMongo 

app = Flask(__name__)

client = pymongo.MongoClient('Localhost:27017')
db = client.sanjay
songs = db.det4


db=PyMongo(app)
xxx=[
    {
        "_id": "11",
        "age": 11,
        "name": "saanjay",
        "gender": "male",
        "email": "111111111111111111111",
        "phone": "1111111111111111",
        "address": "sssssssssssssssssssss",
        "ride_taken": 0,
        "user_plan": 0
    }]

@app.route("/")
def index():
	return render_template("index.html")

@app.route('/add')
def add():
	s=songs.find({'name':'sanjay'})
	if s:
		output = {'name': s['name']}
	else:
		output = "No such name"

	return jsonify({'result' : output})

if __name__ == '__main__':
	app.run(debug=True)