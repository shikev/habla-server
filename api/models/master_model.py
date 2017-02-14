from __future__ import print_function
import sys
import config
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base



habla_engine = create_engine(config.db)

# create a configured "Session" class
Session = sessionmaker(bind=habla_engine)


Base = automap_base()

metadata = MetaData(bind=habla_engine)

Base.prepare(habla_engine, reflect=True)

# # These classes represent the tables in our database
Comment = Base.classes.Comments
Group = Base.classes.Groups
Member = Base.classes.Members
# GroupCommentsMap = Base.classes.GroupComments

