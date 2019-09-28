import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

import math
found = []

logger = logging.getLogger(__name__)

@app.route('/gun-control', methods=['POST'])
def evaluate():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    inputValue = request.get_json();
    result = solution(inputValue)
    logging.info("My result :{}".format(result))
    return json.dumps(result);

def solution(inputValue):
	# Identify all paths
	startpoint = [0,0]

	recursion2(startpoint,1,inputValue["grid"],"X")
	output = maxCombination(inputValue["fuel"])
	return (output)

def recursion2(position,movement,grid,previous):
	flag = False

	# RIGHT
	if (previous != "L"):
		right = position.copy()
		right[0] += 1
		if (right[0] < len(grid[0]) and grid[right[1]][right[0]] == "O"):
			recursion2(right,movement+1,grid,"R")
			flag = True

	# BOTTOM
	if (previous != "U"):
		bottom = position.copy()
		bottom[1] += 1 
		if (bottom[1] < len(grid) and grid[bottom[1]][bottom[0]] == "O"):
			recursion2(bottom,movement+1,grid,"B")
			flag = True

	# LEFT
	if (previous != "R"):
		left = position.copy()
		left[0] -= 1
		if (left[0] >= 0 and grid[left[1]][left[0]] == "O"):
			recursion2(left,movement+1,grid,"L")
			flag = True

	if (previous != "B"):
		up = position.copy()
		up[1] -= 1
		if (up[1] >= 0 and grid[up[1]][up[0]] == "O"):
			recursion2(up,movement+1,grid,"U")
			flag = True

	if (flag == False):
		newDict = dict()
		finalPosition = dict()
		finalPosition["x"] = position[0]+1
		finalPosition["y"] = position[1]+1
		newDict["cell"] = finalPosition
		newDict["guns"] = movement
		found.append(newDict)

def maxCombination(limit):
	# Total no. of combi 
	combi = int(math.pow(2,len(found)))
	maxGuns = 0
	maxChoice = "0" * len(found)

	
	# For all combinations, get total guns and check whether in limit
	for r in range(0,combi):
		totalGuns = 0
		choice = NumToBinary(r,len(found))
		for index in range(len(found)):
			totalGuns += found[index]["guns"] * int(choice[index])

		if (totalGuns > maxGuns and totalGuns <= limit):
			maxGuns = totalGuns
			maxChoice = choice

	output = dict()
	temp = []
	for index in range(len(found)):
		if (maxChoice[index] == "1"):
			temp.append(found[index])

	temp.reverse()
	output["hits"]=temp
	return (output)

def NumToBinary(num,length):
    num = str(bin(num))
    num = num.split("b")
    num = str(num[1])
    num = "0" * (length-len(num)) + num
    return num
