from flask import Flask,send_file
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from pymongo import MongoClient


app = Flask(__name__)
app.config['MONGO_DBNAME'] ='users'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/users'


db=PyMongo(app)


@app.route("/")
def index():
    return send_file("templates/index.html")



@app.route('/user', methods=['GET'])
def get_all_users():
  client = MongoClient('mongodb://localhost:27017/')
  print "client made"
  db = client.users
  col=db.det4
  output = []
  for s in col.find():
    output.append({
        "_id": s[_id],
        "age": s[age],
        "name": s[name],
        "gender": s[gender],
        "email": s[email],
        "phone": s[phone],
        "address": s[address],
        "ride_taken": s[ride_taken],
        "user_plan": s[user_plan]
    })
    
  return jsonify({'result' : output})

@app.route('/user/', methods=['GET'])
def get_one_user(name):
  db = client.users
  col=db.det
  output = []
  s = col.find_one({'name' : name})
  if s:
    output = {'name' : s['name'], 'distance' : s['distance']}
  else:
    output = "No such name"
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