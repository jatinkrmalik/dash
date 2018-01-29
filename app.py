from flask import Flask ,render_template, request
app = Flask(__name__)

@app.route("/")
def index():
	tv_show="Game of Thrones"
	lst=[1,2,3,4,1,5,22,11,44]
	return render_template("index.html",mylst =lst)

if __name__ == '__main__':
	app.run()
