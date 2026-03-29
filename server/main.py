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

#This will get the initial data for the graphs that need it. 
@app.route('/getInitialDataForGraphs', methods=['GET'])
def getInitialDataForGraphs():
    if request.method == 'GET':
        data_dictionary = {}
        get_data_object = ExamineData()
        # Setting Data 
        screen_time_vs_happeniness_data = get_data_object.screen_time_vs_happeniness()
        data_dictionary['Screen_vs_Happeniness'] = screen_time_vs_happeniness_data
        # Setting Data 
        sleep_vs_stress = get_data_object.sleep_vs_stress()
        data_dictionary['sleep_vs_stress'] = sleep_vs_stress
        # Setting Data 
        detox_days_vs_stress  = get_data_object.detox_days_vs_stress()
        data_dictionary['detox_days_vs_stress'] = detox_days_vs_stress 
        return jsonify(data_dictionary)


if __name__ == '__main__':
    app.run(debug=True)