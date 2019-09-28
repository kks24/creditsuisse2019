import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/chessgame', methods=['POST'])
def evaluate():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    inputValue = request.get_json();
    result = solution(inputValue)
    logging.info("My result :{}".format(result))
    return json.dumps(result);


def solution(chessboard):
    n = len(chessboard)

    ans = 0
    for i in range(n):
        for j in range(n):
            diff=j-i
            if (chessboard[i][j] == "K"):
                #to the right
                for k in range(j+1,n):
                    if(chessboard[i][k]=="X"):
                        break
                    else:
                        #print(i,k)
                        ans=ans+1
                #to the left
                for k in range(j-1,-1,-1):
                    if(chessboard[i][k]=="X"):
                        break
                    else:
                        #print(i,k)
                        ans=ans+1
                #up
                for m in range(i-1,-1,-1):
                    if(chessboard[m][j]=="X"):
                        break
                    else:
                        #print(m,j)
                        ans=ans+1
                #down
                for m in range(i+1,n):
                    if(chessboard[m][j]=="X"):
                        break
                    else:
                        #print(m,j)
                        ans=ans+1
                #print(ans)
                #Diagonals
                for d in range(i,n):
                    e=d+diff
                    if(e>=n):
                        break
                    elif(chessboard[d][e]=="K"):
                        continue
                    elif(chessboard[d][e]=="X"):
                        break
                    else:
                        #print(d,e)
                        ans=ans+1
                for d in range(i,-1,-1):
                    e=d+diff
                    if(e<0):
                        break
                    elif(chessboard[d][e]=="K"):
                        continue
                    elif(chessboard[d][e]=="X"):
                        break
                    else:
                        #print(d,e)
                        ans=ans+1
                d=i
                e=j
                while(d>=0 and e>=0 and d<n and e<n):
                    #print("Pass by down", d, e)
                    if(chessboard[d][e]=="K"):
                        d=d+1
                        e=e-1
                        continue
                    elif(chessboard[d][e]=="X"):
                        break
                    else:
                        #print(d,e)
                        ans=ans+1
                    d=d+1
                    e=e-1
                d=i
                e=j
                while(d>=0 and e>=0 and d<n and e<n):
                    #print("Pass by up", d, e)
                    if(chessboard[d][e]=="K"):
                        d=d-1
                        e=e+1
                        continue
                    elif(chessboard[d][e]=="X"):
                        break
                    else:
                        #print(d,e)
                        ans=ans+1
                    d=d-1
                    e=e+1
    return ans            
            
            



