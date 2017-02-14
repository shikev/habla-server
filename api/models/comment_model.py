from __future__ import print_function
import sys
from sqlalchemy import *
from master_model import *
# this line subject to change when deploying
# engine = create_engine('mysql://root:root@localhost:3306/habla')

# metadata = MetaData(habla_engine)
# # comments = Table('Comments', metadata, autoload=True)
# # conn = engine.connect()

# Base = declarative_base(metadata=metadata)

# class Comment(Base):
#     __tablename__ = 'Comments'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     content = Column(String(128), nullable=False)
#     url = Column(String(500), nullable=False)
#     originalPostTime = Column(Timestamp, nullable=False)
#     lastUpdated = Column(Timestamp, nullable=False)
Comment = Base.classes.Comments


def getCommentsByUrl(urlIn):
	session = Session()
	comments = session.query(Comment).filter_by(url=urlIn)
	result = [{"id": c.id, "content": c.content} for c in comments]
	session.close()
	return result
	# sql = select([comments.c.id, comments.c.content]).where(comments.c.url == urlIn)
	# result = conn.execute(sql).fetchall()
	# result = [{"id": r[0], "content": r[1]} for r in result]
	# return result

def addComment(urlIn, contentIn):
	session = Session()
	newComment = Comment(content=contentIn, url=urlIn)
	newId = newComment.id
	session.add(newComment)
	session.commit()
	session.close()
	# sql = comments.insert().values({"url": urlIn, "content": contentIn})
	# result = conn.execute(sql)
	return {"content": contentIn, "id": newId}
