from flask import Flask,send_file
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from pymongo import MongoClient
import pymongo


app = Flask(__name__)

client =pymongo.MongoClient('localhost:27017') 
db = client.users
col=db.det

db=PyMongo(app)


@app.route("/")
def index():
    return send_file("templates/index.html")



@app.route('/user', methods=['GET'])
def get_all_users():
  output = []
  for s in col.find():
    output.append({
        
        "age": s["age"],
        "name": s["name"],
        "gender": s["gender"],
        "email": s["email"],
        "phone": s["phone"],
        "address": s["address"],
        "ride_taken": s["ride_taken"],
        "user_plan": s["user_plan"]
    })
    
  return jsonify({'result' : output})

@app.route('/user/', methods=['GET'])
def get_one_user():
  name1 = request.args.get('name')
  output = []
  s=col.find_one({'name' : name1})
  #if s:
  output.append({
      
      "age": s["age"],
      "name": s["name"],
      "gender": s["gender"],
      "email": s["email"],
      "phone": s["phone"],
      "address": s["address"],
      "ride_taken": s["ride_taken"],
      "user_plan": s["user_plan"]

  })
  #else:
  #output = "No such name"
  return jsonify({'result' : output})

@app.route('/user', methods=['POST'])
def add_user():
  user = mongo.db.users
  name = request.json['name']
  distance = request.json['distance']
  user_id = user.insert({'name': name, 'distance': distance})
  new_user = user.find_one({'_id': user_id })
  output = {'name' : new_user['name'], 'distance' : new_user['distance']}
  return jsonify({'result' : output})
	
if __name__ == "__main__":
    app.run(host='0.0.0.0')