from __future__ import print_function
import sys
from flask import *
from extensions import db
from extensions import crossdomain
from models import comment_model
import urllib

comments = Blueprint('comment_api', __name__, template_folder='templates')

@comments.route('/api/v1/comments', methods=['GET','POST'])
@crossdomain(origin='*')
def comment_route():
	if request.method == 'GET':
		# get url from url params
		url = request.args.get('url')


		# get all comments from database by url
		comments = {"comments": comment_model.getCommentsByUrl(url)}

		# sort by creation date

		# return jsonified list of comments
		return json.jsonify(comments), 200
	elif request.method == "POST":
		# TODO advanced data processing here

		# pull url and body from post parameters
		url = request.form.get('url')
		content = request.form.get('content')
		# Sanitize both for database storage

		# Store both in the database
		# If storage is successful, return success http code. 
		comment_model.addComment(url, content)

		return json.jsonify({}), 200
		