import os

import geopy
import geopy.distance
import numpy as np
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/findOptimalPath', methods=['POST'])
def findOptimalPath():
    

    allLocationPoints = [tuple(item) for item in request.json]
    locationPonits = request.json.get('points')
    startPoint = request.json.get('startPoint')
    targetPoint = request.json.get('targetPoint')
    startPointIndex = 0
#     locationPonits =[ (33.496037313077935, 36.28980510501954), 
#     (33.491814210211864, 36.29821651286583),  
#   (33.53579823020568, 36.239025708131045), 
#     (33.598275895594064, 36.327500719761694), ]

    # startPoint= allLocationPoints[0]   
    # targetPoint= allLocationPoints[len(allLocationPoints)-1]    

    leftedPoinsts =  request.json.get('points')
    # locationPonits.remove(startPoint)
    # locationPonits.remove(targetPoint)
    # leftedPoinsts.remove(startPoint)
    # leftedPoinsts.remove(targetPoint)
 
    costList =array_5x5 = [[1000000 for _ in range(5)] for _ in range(5)]
    visistedPoints =[startPoint]
    allPathCost =0
    completedPoints = False
    copyList = []
    for i in range(len(locationPonits)-1):
        allPathCost =0
        for j in range(len(leftedPoinsts)-1):
            for h in range(len(visistedPoints)-1):
                allPathCost = geopy.distance.geodesic(visistedPoints[h],visistedPoints[h+1]).km
            realCost = geopy.distance.geodesic(startPoint,leftedPoinsts[j]).km +allPathCost
            estimatedCost = geopy.distance.geodesic(startPoint,targetPoint).km
            totalCost = realCost+estimatedCost
            costList[startPointIndex][j+1] = totalCost
            copyList = costList[startPointIndex]
        for i in range(len(copyList)):
            startPointIndex =copyList.index(min(copyList))
            startPoint = locationPonits[startPointIndex]
            print('point')
            print(startPoint)
            print('point')
            if(len(leftedPoinsts)==1):
                visistedPoints.append(leftedPoinsts)
                break
            if startPoint in leftedPoinsts:
                leftedPoinsts.remove(startPoint)
                print(leftedPoinsts)
                visistedPoints.append(startPoint)
                break
            else:
                copyList.pop(startPointIndex)

    visistedPoints.append(targetPoint)
    print(len(visistedPoints))
    print(visistedPoints)
    return jsonify(visistedPoints)



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)




