from __future__ import print_function
import sys
from flask import *
# from extensions import db

from models import group_model
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



groups = Blueprint('group_api', __name__, template_folder='templates')

@groups.route('/api/v1/group/join', methods=['POST'])
def group_join_route():
	if request.method == 'POST':
		# Get parameters from request
		username = request.form.get('username')
		groupName = request.form.get('groupName')
		groupPassword = request.form.get('groupPassword')

		# joined = "success" if success, error message if not
		message = group_model.joinGroup(username, groupName, groupPassword)
		errorCode = 200
		if message != "success":
			errorCode = 400

		# TODO split http codes based on error
		return json.jsonify({"message": message}), errorCode
		
@groups.route('/api/v1/group/create', methods=['POST'])
def group_create_route():
	if request.method == "POST":
		username = request.form.get('username')
		groupName = request.form.get('groupName')
		groupPassword = request.form.get('groupPassword')

		# created = "success", error message if not
		message = group_model.createGroup(username, groupName, groupPassword)

		# TODO split http codes based on error
		return json.jsonify({"message": message}), 200




@groups.route('/api/v1/group/links', methods=['GET', 'POST'])
@crossdomain(origin='*')
def group_links_route():
    if request.method == "GET":
        groupName = request.args.get('groupName')
        links = group_model.getGroupLinks(groupName)

        # TODO split http codes based on error
        return json.jsonify({"links": links}), 200
    elif request.method == "POST":
        print(request.form, sys.stderr)
        message = group_model.addGroupLink(request.form.get("groupName"), request.form.get("link"))
        return json.jsonify({"message": message}), 200

@groups.route('/api/v1/group/password', methods=['GET'])
@crossdomain(origin='*')
def group_password_route():
    if request.method == "GET":
        groupName = request.args.get('groupName')
        password = group_model.getGroupPassword(groupName)

        # TODO split http codes based on error
        return json.jsonify({"password": password}), 200
