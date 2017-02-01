from flask import *
from extensions import db

comment = Blueprint('comment_api', __name__, template_folder='templates')

@comment.route('/api/v1/comment', methods=['GET','POST'])
def comment_route():
	if request.method == 'GET':
		return json.jsonify({"content":"Some Filler"}), 200
	elif request.method == "POST":
		# TODO data processing here
		return json.jsonify({}), 200
		