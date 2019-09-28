import logging
import json
import math

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/exponent', methods=['POST'])
def evaluate_exponent():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    inputValue = request.get_json();
    result = Exponent(inputValue)
    logging.info("My result :{}".format(result))
    return jsonify(result);

def Exponent(inputValue):
	trailingList = [[0],[2,4,8,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1]]

	n = inputValue["n"]
	p = inputValue["p"]

	# LAST DIGIT
	num = n % 10
	multiple = (p-1) % len(trailingList[num-1])
	last_digit = trailingList[num-1][multiple]

	# FIRST DIGIT
	log_start = p * (math.log(n) / math.log(10))

	first_digit = int(math.pow(10,log_start % 1))
	print (first_digit)

	# LENGTH
	length = math.ceil(log_start)

	output = dict()
	output["result"] = [first_digit,length,last_digit]
	return output
