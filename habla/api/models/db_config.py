import os

def getDB():

	if 'RDS_HOSTNAME' in os.environ:
		DB = {
			'NAME': os.environ['RDS_DB_NAME'],
			'USER': os.environ['RDS_USERNAME'],
			'PASSWORD': os.environ['RDS_PASSWORD'],
			'HOST': os.environ['RDS_HOSTNAME'],
			'PORT': os.environ['RDS_PORT'],
		}

		db_connect = "mysql://{0}:{1}@{2}:{3}/{4}".format(DB['USER'], DB['PASSWORD'], DB['HOST'], DB['PORT'], DB['NAME'])

	return db_connect

