from __future__ import print_function
import sys
import config
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, relationship, backref
# from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.ext.associationproxy import association_proxy



habla_engine = create_engine(config.db)

# Create a configured "Session" class
Session = sessionmaker(bind=habla_engine)


Base = declarative_base()


# groupsUsersTable = Table('GroupsUsers', Base.metadata,
#     Column('groupId', Integer, ForeignKey("Groups.id"), primary_key=True),
#     Column('userId', Integer, ForeignKey("Users.id"), primary_key=True),
#     Column('privilege', String(20))
# )

# Association class for Groups and Users (many-to-many)
class GroupUser(Base):
    __tablename__ = 'GroupsUsers'
    groupId = Column(Integer, ForeignKey('Groups.id'), primary_key=True)
    userId = Column(Integer, ForeignKey('Users.id'), primary_key=True)
    privilege = Column(String(20))
    # Alias is a users name in that group
    alias = Column(String(55))
    group = relationship("Group", back_populates="users")
    user = relationship("User", back_populates="groups")


class Comment(Base):

    __tablename__ = 'Comments'

    id          =   Column(Integer, primary_key=True)
    content        =   Column(Text)
    url       =   Column(String(500))
    originalPostTime  =   Column(DateTime, default=datetime.utcnow)
    lastUpdated  =   Column(DateTime, default=datetime.utcnow)
    # TODO: Re-think this when doing auth'd users
    posterName = Column(String(55))

    # TODO: Consider using adjacency list for parentId in the future

    # Relationships
    # A comment has a parent (itself, or NULL). This is not coded in as a relation currently
    # A comment has a user, and has a group
    parentId = Column(Integer)
    userId = Column(Integer, ForeignKey('Users.id'))
    groupId = Column(Integer, ForeignKey('Groups.id'))

    def __repr__(self):
        return str(self.id) + self.content

class Group(Base):

    __tablename__ = 'Groups'

    id          =   Column(Integer, primary_key=True)
    creator        =   Column(String(32))
    password       =   Column(String(128))
    name  =   Column(String(128))

    # Relationships
    # A group has many comments and many users
    comments    =   relationship('Comment', backref="group")
    users = relationship("GroupUser", back_populates="group")

    def __repr__(self):
        pass

class User(Base):

    __tablename__ = 'Users'

    id      =   Column(Integer, primary_key=True)
    # uuid is generated, given back to the client and stored permanently. Might be redundant with username/password later
    # TODO change uuid to nullable=False
    uuid    =   Column(String(64), unique=True)

    # Relationships
    # A user has many comments and many groups
    comments = relationship('Comment', backref="user")
    groups = relationship("GroupUser", back_populates="user")

    def __repr__(self):
        pass

# This should only occur if the tables do not exist...
Base.metadata.create_all(habla_engine)

# TODO: Test Behavior with adding columns to existing tables

