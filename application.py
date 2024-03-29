"""
This script runs the FlaskWebProject1 application using a development server.
"""

from os import environ
from habla import application

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(environ.get('SERVER_PORT', '3000'))
    except ValueError:
        PORT = 3000
    application.run(HOST, PORT)
