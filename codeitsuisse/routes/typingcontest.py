import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/typing-contest', methods=['POST'])
def evaluate():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    inputValue = request.get_json();
    result = solution(inputValue)
    logging.info("My result :{}".format(result))
    return jsonify(result);


def hamming_distance(string1, string2):
    # Start with a distance of zero, and count up
    distance = 0
    # Loop over the indices of the string
    L = len(string1)
    for i in range(L):
        # Add 1 to the distance if these two characters are not equal
        if string1[i] != string2[i]:
            distance += 1
    # Return the final count of differences
    return distance


def calculate(pre, thing, cost, path):
    if len(thing) == 1:
        cost = cost + 1 + hamming_distance(thing[0], pre)
        path.append([thing[0]])
        return cost, path
    costlist = []
    pathlist = []
    for i in thing:
        costi = cost + 1 + hamming_distance(i, pre)
        path.append([i])
        cost1, path1 = calculate(i, list(set(thing) - set([i])), costi, [i])
        costlist.append(cost1)
        pathlist.append(path1)

    return min(costlist), pathlist[costlist.index(min(costlist))]


def solution(sample_input):
    output = {"cost": 0, "steps": []}

    pathlist = []
    for i in sample_input:
        cost = len(i)
        # step.append([{"type": 'INPUT', "value": i}])
        sample_copy = sample_input.copy()
        sample_copy.remove(i)
        path = []
        cost1, path1 = calculate(i, sample_copy, cost, path)
        outputcost.append(cost1)
        path2 = [i, path1]
        pathlist.append(path2)
    min_path = pathlist[outputcost.index(min(outputcost))]

    output["steps"].append({'type': 'INPUT', 'value': min_path[0]})
    while (len(min_path) != 1):
        output["steps"].append({'type': 'COPY', 'value': min_path[0]})
        output["steps"].append({'type': 'TRANSFORM', 'value': min_path[1][0]})
        min_path = min_path[1]

    output["cost"] = min(outputcost)

    return output
