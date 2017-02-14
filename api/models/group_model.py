from __future__ import print_function
import sys
from sqlalchemy import *
from master_model import *


def createGroup(username, groupName, groupPassword):
	session = Session()
	newGroup = Group(name=groupName, password=groupPassword, creator=username)
	newMember = Member(username=username, groupId=newGroup.id)
	session.add(newGroup)
	session.add(newMember)
	session.commit()
	session.close()
	return "success"

def joinGroup(username, groupName, groupPassword):
	session = Session()
	groupToJoin = session.query(Group).filter_by(name=groupName, password=groupPassword).first()
	if groupToJoin == None:
		return "Group does not exist or password incorrect."

	memberExists = session.query(Member).filter_by(groupId=groupToJoin.id)
	if memberExists:
		return "Username already taken for this group!"

	newMember = Member(username=username, groupId=groupToJoin.id)
	session.add(newMember)
	session.commit()
	session.close()
	return "success"
