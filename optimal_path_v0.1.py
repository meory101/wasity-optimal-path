import geopy
import geopy.distance

locationPonitsNames=["mazzeh", "aspu", "marabaa","barada"]
locationPonits = [
    (33.600681416134506, 36.329047202425656), 
    (33.57698377737123, 36.28683948478614),
    (33.22009393939333, 36.12898989896666),
    (33.22009393939333, 36.12898989896666),
    (33.62751978497324, 36.10575190558477)
]
initStartPoint =(33.50496963350299, 36.26174203924571)
targetPoint=(33.62751978497324, 36.10575190558477)

newStartPoint = initStartPoint

visitedPointsList=[(33.50496963350299, 36.26174203924571)]
totalCostList =[]
while newStartPoint!=targetPoint:
    for i in range(len(locationPonits)):
        if(not locationPonits[i] in visitedPointsList):
            localRealCost = geopy.distance.geodesic(newStartPoint,locationPonits[i]).km
            for j in range(len(visitedPointsList)):
                localRealCost+=geopy.distance.geodesic(newStartPoint,visitedPointsList[j]).km
            localEstimationCost = geopy.distance.geodesic(newStartPoint,targetPoint).km
            totalCost = localRealCost+localEstimationCost
            totalCostList.append(totalCost)
            newStartPointIndex =totalCostList.index(min(totalCostList))
            visitedPointsList.append(newStartPoint)
            if(newStartPointIndex>=len(locationPonits)):
                print('000000000')
                newStartPoint=targetPoint
                break
            else:   
                print(newStartPointIndex)
                newStartPoint = locationPonits[newStartPointIndex]
                


# minTotalCost= 0
# minTotalCostIndex=0
# selectedNodeIndex = 0

# visitedNodes =[]
# for i in range(minTotalCostIndex,len(locationPonits)):
#     for j in range(i,len(locationPonits)):
#         realCost= geopy.distance.geodesic(locationPonits[i],locationPonits[j]).km
#         eastCost = geopy.distance.geodesic(locationPonits[i],(33.62751978497324, 36.10575190558477)).km
#         localMinTotalCost =realCost+eastCost
#         if(minTotalCost==0):
#             minTotalCost=localMinTotalCost

#         elif(localMinTotalCost<minTotalCost):
#             minTotalCost =localMinTotalCost
#             minTotalCostIndex = j


# for i in range(len(locationPonits)):
    # for j in range (len(locationPonits)):
    #     if(i!=j):
    #         visitedNodes.append(locationPonits[j])
    #         realCost= geopy.distance.geodesic(locationPonits[i],locationPonits[j]).km
    #         eastCost = geopy.distance.geodesic(locationPonits[i],(33.62751978497324, 36.10575190558477)).km
    #         localCost = realCost+eastCost
    #         if(minTotalCost ==0):
    #             minTotalCost = realCost+eastCost
    #         elif(localCost<minTotalCost):
    #            minTotalCostIndex=j
    #             minTotalCost= localCost


 










