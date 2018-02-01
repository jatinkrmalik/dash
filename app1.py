from flask import Flask,render_template
from flask import jsonify
from flask import request
from pymongo import MongoClient
import pymongo
from flask_pymongo import PyMongo 


app = Flask(__name__)

client = pymongo.MongoClient('Localhost:27017')
db = client.sanjay
collectio = db.det4


db=PyMongo(app)


@app.route("/")
def index():
    return render_template("myindex.html")



@app.route('/all_user', methods=('get', 'post'))
def get_all_users():
    client = MongoClient('mongodb://localhost:27017/')
    print "client made"
    db = client.sanjay
    col=db.det
    output = []
    for s in col.find():
        output.append({
         "_id": s['_id'],
        "age": s['age'],
        "name": s['name'],
        "gender": s['gender'],
        "email": s['email'],
        "phone": s['phone'],
        "address": s['address'],
        "ride_taken": s['ride_taken'],
        "user_plan": s['user_plan']
        })
    return jsonify({'result' : output})

@app.route('/one_user/', methods=('get', 'post'))
def get_one_user():
    client = MongoClient('mongodb://localhost:27017/')
    print "client made"
    db = client.sanjay
    col=db.det
    output = []
    email = request.args.get('email')
    s = col.find_one({'email' : email})
    if s:
        output = { 
        "_id": s['_id'],
        "age": s['age'],
        "name": s['name'],
        "gender": s['gender'],
        "email": s['email'],
        "phone": s['phone'],
        "address": s['address'],
        "ride_taken": s['ride_taken'],
        "user_plan": s['user_plan']}
    else:
        output = "No such name"
    return jsonify({'result' : output})

@app.route('/yyyyy', methods=['POST'])
def add_user():
    user = mongo.db.sanjay
    name = request.json['name']
    distance = request.json['distance']
    user_id = user.insert({'name': name, 'distance': distance})
    new_user = user.find_one({'_id': user_id })
    output = {'name' : new_user['name'], 'distance' : new_user['distance']}
    return jsonify({'result' : output})
	
if __name__ == "__main__":
    app.run()