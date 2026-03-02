from flask import Flask, jsonify, request
from flask_cors import CORS
import math

# Importing files that I made:
from data import *
# from db import *

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

#This will get the initial data for the graphs. 
@app.route('/getInitialDataForGraphs', methods=['GET'])
def getInitialDataForGraphs():
    if request.method == 'GET':
        data_dictionary = {}
        get_data_object = ExamineData()
        screen_time_vs_happeniness_data = get_data_object.screen_time_vs_happeniness()
        data_dictionary['Screen_vs_Happeniness'] = screen_time_vs_happeniness_data
        return jsonify(data_dictionary)


if __name__ == '__main__':
    app.run(debug=True)