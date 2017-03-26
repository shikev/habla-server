from __future__ import print_function
import sys
from flask import *
# from extensions import db
from models import comment_model
import urllib

from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers
            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            h['Access-Control-Allow-Credentials'] = 'true'
            h['Access-Control-Allow-Headers'] = \
                "Origin, X-Requested-With, Content-Type, Accept, Authorization"
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

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
		