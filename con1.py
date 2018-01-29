from flask import Flask 
from flask.ext.pymongo import PyMongo 

app = Flask(__name__)

app.config['MONGO_DBNAME'] ='mydatabase'
app.config['MONGO_URI'] = 'mongodb://sanjay:sanjay@ds117128.mlab.com:17128/mydatabase'

db=PyMongo(app)

@app.route("/")
def index():
	return render_template("index.html")

@app.route('/add')
def add():
	user = mongo.db.users
	user.insert({'name' : 'jat'})
	return 'Added User'

if __name__ == '__main__':
	app.run(debug=True)