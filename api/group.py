from __future__ import print_function
import sys
from flask import *
from extensions import db
from extensions import crossdomain
from models import group_model
import urllib

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

		# TODO split http codes based on error
		return json.jsonify({"message": message}), 200
		
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