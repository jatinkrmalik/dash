import os
import sys
import flask
from flask import request
from flask import jsonify
from flask import render_template

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '../../')))


app = flask.Flask(__name__)
app.config.from_object(__name__)
app.config['MONGODB_SETTINGS'] = {'DB': 'sanjay'}

#app.config['TESTING'] = True

app.debug = True
app.config['DEBUG_TB_PANELS'] = (
    'flask_debugtoolbar.panels.versions.VersionDebugPanel',
    'flask_debugtoolbar.panels.timer.TimerDebugPanel',
    'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
    'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
    'flask_debugtoolbar.panels.template.TemplateDebugPanel',
    'flask_debugtoolbar.panels.logger.LoggingPanel',
    'flask_mongoengine.panels.MongoDebugPanel'
)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


from models import db
db.init_app(app)
from views import *

@app.route("/")
def index():
    return render_template("firstpage.html")


@app.route("/table/", methods=['GET'])

def table_call():
    tbname = request.args.get('tablename')
    return commands[tbname]()


#Views.func_map(tbName)
    




#app.add_url_rule('/func', view_func=view_user_det)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
