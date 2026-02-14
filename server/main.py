from flask import Flask, jsonify, request
from flask_cors import CORS
import math

# Importing files that I made:
# from data import *
# from db import *

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


if __name__ == '__main__':
    app.run(debug=True)