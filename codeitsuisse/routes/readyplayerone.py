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
    T = int(T)
    Nlist=[x+1 for x in range(N)]

    path=[]
    def calculate(Nlist,T):
        start=T%(Nlist[0]+Nlist[-1])
        Tleft=T-start
        length=len(Nlist)
        if length//2!=length/2 and start==Nlist[(length)//2]:
            return {"res":1+2*(Tleft/(Nlist[0]+Nlist[-1]))}
        elif start in [Nlist[0],Nlist[-1]] and len(Nlist)>1:
            if start == Nlist[0]:
                Nlist=[x+1 for x in range(1,N)]
            elif start == Nlist[-1]:
                Nlist=[x+1 for x in range(N-1)]
            ans=calculate(Nlist,Tleft)
            if ans["res"]==-1:
                return ans
            else:
                ans["res"]+=1
                return ans
        elif Tleft==sum([Nlist[0],Nlist[-1]]):
            return {"res":3}
        else:
            return {"res":-1}
                    
    return calculate(Nlist,T)
