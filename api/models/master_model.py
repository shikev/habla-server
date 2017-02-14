from __future__ import print_function
import sys
import config
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
# this line subject to change when deploying
# engine = create_engine('mysql://root:root@localhost:3306/habla')
# an Engine, which the Session will use for connection
# resources
habla_engine = create_engine(config.db)

# create a configured "Session" class
Session = sessionmaker(bind=habla_engine)
# metadata = MetaData(habla_engine)
# comments = Table('Comments', metadata, autoload=True)
# conn = engine.connect()

Base = automap_base()
Base.prepare(habla_engine, reflect=True)

Comment = Base.classes.Comments
Group = Base.classes.Groups
Member = Base.classes.Members

