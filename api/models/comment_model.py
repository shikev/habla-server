from __future__ import print_function
import sys
from sqlalchemy import *
from master_model import *

# RETURNS: 
# List of dictionaries. Dictionaries have keys "id" and "content"
def getCommentsByUrl(urlIn, groupName):

	session = Session()
	comments = session.query(Comment).filter_by(url=urlIn).filter(Group.name==groupName)

	result = [{"id": c.id, "content": c.content} for c in comments]
	session.close()
	return result

# RETURNS:
# Dictinoary. Dictionary has keys "id" and "content"
def addComment(urlIn, contentIn, groupName):
	session = Session()
	group = session.query(Group).filter_by(name=groupName).first()
	# Create the new comment and the new group-comments mapping
	newComment = Comment(content=contentIn, url=urlIn)
	newComment.groups_collection.append(group)
	newId = newComment.id
	
	session.add(newComment)
	session.commit()
	session.close()
	return {"content": contentIn, "id": newId}
