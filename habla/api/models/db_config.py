import base64
import json

def getDB():
	with open('config.json') as config_file:
		config = json.load(config_file)
		db = config["db"]

		user = 'habla'
		pw = 'habla2017!'
		endpoint = 'habladb.cy6rmyo1guo1.us-east-1.rds.amazonaws.com:3306'
		# user = db["user"]
		# pw = base64.b64decode(db["password"])
		# endpoint = db["endpoint"]

		db_connect = "mysql://{0}:{1}@{2}/habla".format(user, pw, endpoint)

	return db_connect

