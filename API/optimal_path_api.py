import os

import geopy
import geopy.distance
import numpy as np
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/findOptimalPath', methods=['POST'])
def findOptimalPath():
    locationPoints = request.form.get('locationPoints')
    
    locationPonits =  request.form.get('locationPoints')
    startPoint=    request.form.get('startPoint'),   
    startPointIndex = 0
    targetPoint= request.form.get('targetPoint'),   
    tuples_list = [tuple(item) for item in request.form.get(locationPoints)]

    return jsonify((tuples_list))


    costList =array_5x5 = [[1000000 for _ in range(5)] for _ in range(5)]
    visistedPoints =[startPoint]
    allPathCost =0
    completedPoints = False
    copyList = []
    for i in range(len(locationPonits)):
        allPathCost =0
        for j in range(len(leftedPoinsts)):
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



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)




