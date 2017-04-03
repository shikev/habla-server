from flask import Flask, render_template
import extensions
import controllers
import api

# Initialize Flask application with the template folder address
application = Flask(__name__, template_folder='templates')

# Register the controllers

application.register_blueprint(api.comments)
application.register_blueprint(api.groups)

application.secret_key = 'C\xafh\xf8\xfd0m\xa8\xf3\xe3\x14,\xda\xa6\xb8\xffq\x8bm\xb9\xc2\x02\xfc\x19'
