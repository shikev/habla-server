from flask import Flask, render_template
import extensions
import controllers
import api
import config

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates')

# Register the controllers

app.register_blueprint(api.comments)


app.secret_key = 'C\xafh\xf8\xfd0m\xa8\xf3\xe3\x14,\xda\xa6\xb8\xffq\x8bm\xb9\xc2\x02\xfc\x19'

# Listen on external IPs
# For us, listen to port 3000 so you can just run 'python app.py' to start the server
if __name__ == '__main__':
    # listen on external IPs
    app.run(host=config.env['host'], port=config.env['port'], debug=True)
