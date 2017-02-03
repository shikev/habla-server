from __future__ import print_function
import sys
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table
from sqlalchemy.sql import select, insert
# this line subject to change when deploying
engine = create_engine('mysql://root:root@localhost:3306/habla')

metadata = MetaData(engine)
comments = Table('Comments', metadata, autoload=True)
conn = engine.connect()

class Comment(object):
    def __init__(self, content=None, url=None, postTime=None):
        self.content = content
        self.url = url
        self.postTime = postTime
    def __repr__(self):
        return self.content

def getCommentsByUrl(urlIn):
	sql = select([comments.c.content]).where(comments.c.url == urlIn)
	result = conn.execute(sql).fetchall()
	result = [r[0] for r in result]
	return result

def addComment(urlIn, contentIn):
	sql = comments.insert().values({"url": urlIn, "content": contentIn})
	conn.execute(sql)
	return True
