from flask import Flask, request, jsonify, url_for  # Flask server init
from flask_cors import CORS, cross_origin  # solution for error: cross origin
from Run_file_addr_data import *  # importing all classes and functions
from Run_file_builders_data import *  # importing all classes and functions
#from Class_Builders_tool import *  # importing builders tool class to activate from Front request
import requests  # handaling requests from front end
import json  # working with json dicts
import yagmail

'''
# Function under /address tag operating only after POST or GET requests 
# The /address function is waiting for POST request from front end
# Then it takes the params from it and use them in the Run_file
# For testing with Postman we need to change the format of the dictionary to
# print(request.args)
# street = request.args.get('street')
# return street
-----------------------------------------------------
Setup params:
street1 = '4557 N Springfield Ave'
street2 = "11105 Sage Canyon Drive"
street3 = "10237 Bright Crystal Ave"
street4 = "10618 Fuzzy Cattail Street"
city1 = 'Chicago'
city2 = "Riverview"
short_state1 = 'IL'
short_state2 = 'FL'
state1 = 'Illinois'
state2 = 'Florida'
xls_name = 'Demographytest2.xlsx'
xls_name2 = 'Crimetest2.xlsx'
xls_name3 = 'Schoolstest2.xlsx'
xls_name4 = 'CMAtest2.xlsx'
xls_name5 = 'Builders_tool.xlsx'
log_file_name = 'Testlog.txt'


test 1
451 clear blue way
McDonough
Georgia
GA

test2
4557 N Springfield Ave
Chicago
Illinois
IL

test3
11105 Sage Canyon Drive
Riverview
Florida
FL

test4
10237 Bright Crystal Ave
Riverview
Florida
FL

test5
10618 Fuzzy Cattail Street
Riverview
Florida
FL
-----------------------------------------------------
'''

# local data
xls_name = 'Demography.xlsx'
xls_name2 = 'Crime.xlsx'
xls_name3 = 'Schools.xlsx'
xls_name4 = 'CMA.xlsx'
xls_name5 = 'Builders.xlsx'
log_file_name = '(NR)-Testlog.txt'

# Flask setup
app = Flask(__name__)
CORS(app)


# test connection function
@app.route("/", methods=["POST", "GET"])
def home():
    return "test requests"

# function for address automation tool
# function under /address tag operating only after POST or GET requests configured
# the /address function is waiting for POST request from front end
# then it takes the params from it and use them in the Run_file big function
@app.route('/address', methods=["POST", "GET"])
def address():
    # creating dictionary to fill in the params from POST request
    flask_addr = {
        'street': '',
        'city': '',
        'short_state': '',
        'state': ''
    }
    if request.method == "POST":
        print('Hi, the address function was activated :)')
        print('The input parameters are: {}'.format(request.json))  # request params in json

        # converting params
        flask_addr['street'] = request.json.get('street')
        flask_addr['city'] = request.json.get('city')
        flask_addr['short_state'] = request.json.get('short_state')
        flask_addr['state'] = request.json.get('state')

        # running the run file function using params from Front converting to json format
        datalist = address_data_automate_tool(flask_addr['street'], flask_addr['city'], flask_addr['short_state'], flask_addr['state'], log_file_name, xls_name, xls_name2, xls_name3, xls_name4)
        print('------------------------------------------------------------------------')
        # converting the data_list list into beautiful :) string
        # the string representing all dicts in the list and print the back same as on console
        data2json = json.dumps(datalist, indent=4, separators=(". ", " = "))
        print('Type of return object {}'.format(type(data2json)))
        print('Results: \n {}'.format(data2json))  # printing the results

        return data2json  # return all dictionaries in one list in jason format, printed on home page


# function for builders tool


# Run Flask server
if __name__ == "__main__":
    app.run(debug=True)
