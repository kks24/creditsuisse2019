import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/readyplayerone', methods=['POST'])
def evaluate_readyp1():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    inputValue = request.get_json();
    result = play(inputValue)
    logging.info("My result :{}".format(result))
    return jsonify(result);


def play(sample_input):
    N=sample_input["maxChoosableInteger"]
    T=sample_input["desiredTotal"]
    N = int(N)
    Nlist=[x+1 for x in range(N)]

    path=[]
    sumstart=0
    while(sumstart<T-(Nlist[-1]+Nlist[0])):
        start=T%(Nlist[-1]+Nlist[0])
        path.append(start)
        Nlist.remove(start)
        sumstart = sumstart+start

    if(len(path)%2==0):
        return -1
    else:
        path.append(Nlist[0])
        path.append(Nlist[-1])
        return {"res":len(path)}
