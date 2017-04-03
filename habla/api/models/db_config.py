import base64
import json

def getDB():
	with open('config.json') as config_file:
		config = json.load(config_file)
		db = config["db"]

		user = db["user"]
		pw = db["password"]
		user = db["user"]
		pw = base64.b64decode(db["password"])
		endpoint = db["endpoint"]

		db_connect = "mysql://{0}:{1}@{2}/habla".format(user, pw, endpoint)

	return db_connect

