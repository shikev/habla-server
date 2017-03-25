from __future__ import print_function
import sys
from flask import *
# from extensions import db
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
		groupName = request.args.get('groupName')

		# get all comments from database by url
		comments = {"comments": comment_model.getCommentsByUrl(url, groupName)}

		# sort by creation date

		# return jsonified list of comments
		return json.jsonify(comments), 200
		
	elif request.method == "POST":
		# TODO advanced data processing here

		
		url = request.form.get('url')
		content = request.form.get('content')
		groupName = request.form.get('groupName')
		posterName = request.form.get('username')
		parentId = request.form.get('parentId')

		if parentId == None:
			parentId = 0
		# Sanitize content for database storage

		# Store both in the database
		# If storage is successful, return success http code. 
		comment = comment_model.addComment(url, content, groupName, posterName, parentId)

		return json.jsonify({"comment": comment}), 200
		