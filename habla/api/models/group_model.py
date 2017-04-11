from __future__ import print_function
import sys
from sqlalchemy import *
from master_model import *
import json

# RETURNS:
# String. Contains either "success" or an error message
def createGroup(username, groupName, groupPassword):
	session = Session()

	# Check if group with this name already exists
	groupCheck = session.query(Group).filter_by(name=groupName).first()
	if groupCheck:
		return "Group with this name already exists!"

	# Create the group
	newGroup = Group(name=groupName, password=groupPassword, creator=username)

	# TODO add uuid to user
	assoc = GroupUser(privilege="admin", alias=username)
	assoc.user = User()
	newGroup.users.append(assoc)
	session.add(assoc)
	session.add(newGroup)
	session.commit()
	session.close()
	return "success"

# RETURNS:
# String. Contains either "success" or an error message
def joinGroup(username, groupName, groupPassword):
	session = Session()

	# Check if the group password matches the group name
	groupToJoin = session.query(Group).filter_by(name=groupName, password=groupPassword).first()
	if groupToJoin == None:
		return "Group does not exist or password incorrect."

	# Check if a member with this username is already in the group
	userExistsInGroup = session.query(GroupUser).filter_by(alias=username, groupId=groupToJoin.id).all()
	if userExistsInGroup:
		return "Username already taken for this group!"

	newUser = User()
	assoc = GroupUser(privilege="user", alias=username)
	assoc.user = newUser
	groupToJoin.users.append(assoc)
	session.add(assoc)
	session.add(groupToJoin)
	session.commit()
	session.close()
	return "success"

def getGroupLinks(groupName):
	session = Session()
	group = session.query(Group).filter_by(name=groupName).first()

	if group == None:
		session.close()
		return None
	toRet = group.links
	if not group.links:
		toRet = []
	session.close()
	return json.loads(toRet)


def addGroupLink(groupName, link):
	session = Session()
	group = session.query(Group).filter_by(name=groupName).first()
	if group == None:
		return "Group does not exist!"

	if group.links:
		linkList = json.loads(group.links)
	else:
		linkList = []
	linkList.append(link)
	group.links = json.dumps(linkList)
	session.commit()
	session.close()
	return "success"

def getGroupPassword(groupName):
	session = Session()
	group = session.query(Group).filter_by(name=groupName).first()

	if group == None:
		session.close()
		return None
	password = group.password
	session.close()
	return password
