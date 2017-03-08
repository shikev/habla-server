from __future__ import print_function
import sys
from sqlalchemy import *
from master_model import *

# RETURNS: 
# List of dictionaries. Dictionaries have keys "id" and "content"
def getCommentsByUrl(urlIn, groupName):

	session = Session()
	comments = session.query(Comment).filter_by(url=urlIn).filter(Group.name==groupName)

	results = []
	# {parentId: {dict[id: children], content:"blah", poster:shikev, timestamp:number}}
	parents = {}

	for c in comments:
		print(c, sys.stderr)
		currentIdInfo = {"id": c.id, "content": c.content, "posterName": c.posterName, "timestamp": c.originalPostTime, "children": [], "parentId": c.parentId}

		if c.parentId not in parents:
			parents[c.parentId] = []
		parents[c.parentId].append(currentIdInfo)

	if len(parents) > 0:
		results = [x for x in parents[0]]

	# results is top level comments atm, append children!
	for i in range(len(results)):
		parentId = results[i]["id"]
		children = parents.get(parentId)
		if children:
			results[i]["children"] = parents.get(parentId)

	session.close()
	return results

# RETURNS:
# Dictinoary. Dictionary has keys "id" and "content"
def addComment(urlIn, contentIn, groupName, posterName, parentId = 0):
	session = Session()
	group = session.query(Group).filter_by(name=groupName).first()

	newComment = Comment(content=contentIn, url=urlIn, parentId=parentId, posterName=posterName)
	newComment.group = group
	newComment.user = User()
	
	session.add(newComment)
	session.commit()
	session.refresh(newComment)
	newId = newComment.id
	newParentId = parentId
	session.close()
	return {"content": contentIn, "id": newId, "posterName": c.posterName, "timestamp": c.originalPostTime, "children": [], "parentId": parentId}
