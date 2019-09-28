import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/wedding-nightmare', methods=['POST'])
def evaluate_wedding():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    inputValue = request.get_json();
    result = wedding(inputValue)
    logging.info("My result :{}".format(result))
    return jsonify(result);


def wedding(wedding):
    outlist=[]

    for test_case in wedding:
        outdict={}
        outdict["test_case"]=test_case.get("test_case")
        guestlist = []
        guestlist.extend(range(1,test_case.get("guests")+1))
        allocation = []
        friends = test_case.get("friends") + test_case.get("families")
        mainfriends = friends.copy()
        finalfriends = friends.copy()
        i=-1
        while(i==-1):
            i=0
            for friendgroups in mainfriends:
                if i==-1:
                    break
                i = i+1
                for friendgrps in mainfriends[i:]:
                    if not set(friendgroups).isdisjoint(friendgrps):
                        mainfriends.remove(friendgroups)
                        mainfriends.remove(friendgrps)
                        mainfriends.append(friendgroups + list(set(friendgrps) - set(friendgroups)))
                        i= -1
                        break
        for tables in mainfriends:
            allocation.append(tables)
        size = len(allocation)

        i=0
        enemies = test_case.get("enemies")
        for enemiess in enemies:
            if i==1:
                break
            for friendgroup in mainfriends:
                if(all(x in friendgroup for x in enemiess)):
                    outdict["satisfiable"] = False
                    outdict["allocation"] = []
                    i=1
                    break
        if i==1:
            outlist.append(outdict)
            continue
        main = []
        for i in range(len(mainfriends)):
            main = main + mainfriends[i]
        guest = list(set(guestlist)-set(main))
        haveenemy=0
        enemiescopy=enemies.copy()
        enemiesperg={}
        for g in guest:
            enemiesperg[g]=[]
            for enemyg in enemiescopy:
                if g in enemyg:
                    enemyg.remove(g)
                    for enemy in enemyg:
                        if enemy not in enemiesperg[g]:
                            enemiesperg[g].append(enemy)
                    enemyg.append(g)
        enemiespergcopy=enemiesperg.copy()
        for key,values in enemiespergcopy.items():
            if len(values)<1:
                del enemiesperg[key]
        
        #print("enemiesperg", enemiesperg)
        for g in guest:
            if g in enemiesperg.keys():
                slotinliao=0
                for i in range(len(allocation)):
                    enemyintablei=0
                    for enemy in enemiesperg[g]:
                        if enemy in allocation[i]:
                            enemyintablei=1
                    if(enemyintablei==0):
                        allocation[i].append(g)
                        slotinliao=1
                if(slotinliao==0):
                    allocation.append([g])
            else:
                allocation[0].append(g)
        
        #print(allocation)
        allocation1=[]
        for i in range(1,1+test_case.get("guests")):
            for j in allocation:
                if i in j:
                    allocation1.append([i,allocation.index(j)+1])
        
        if(len(allocation)>test_case.get("tables")):
            outdict["satisfiable"] = False
            outdict["allocation"] = []
        else:
            outdict["satisfiable"] = True
            outdict["allocation"] = allocation1
                
                        
            
        outlist.append(outdict)
    return outlist
