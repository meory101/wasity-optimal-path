import geopy
import geopy.distance
import numpy as np






locationPonits = [
  (33.496037313077935, 36.28980510501954), 
    (33.491814210211864, 36.29821651286583),  
  (33.53579823020568, 36.239025708131045), 
    (33.598275895594064, 36.327500719761694), 
]
startPoint=    (33.505989409455445, 36.28621972360292),   #aspu baramkeh
startPointIndex = 0
targetPoint= (33.7435403196779, 36.467399542219596)  #akubar
leftedPoinsts  =  [
  (33.496037313077935, 36.28980510501954), 
    (33.491814210211864, 36.29821651286583),  
  (33.53579823020568, 36.239025708131045), 
    (33.598275895594064, 36.327500719761694),]


costList =array_5x5 = [[1000000 for _ in range(5)] for _ in range(5)]
visistedPoints =[startPoint]
allPathCost =0
completedPoints = False
copyList = []
for i in range(4):
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










# test data 1

#    (33.57762908718446, 36.28801340253833), # maraba
#     (33.60081009559518, 36.32846086593366),  # aspu tal
#   (33.547328432821196, 36.30664424666099), # hospital
#     (33.66650293799695, 36.07404349419762),
# output

# 0 aspu b
# 1 maraba
# 2 aspu
# 3 aspu
# 4 jabadani














# newStartPoint = initStartPoint

# visitedPointsList=[(33.50496963350299, 36.26174203924571)]
# totalCostList =[]
# while newStartPoint!=targetPoint:
#     for i in range(len(locationPonits)):
#         if(not locationPonits[i] in visitedPointsList):
#             localRealCost = geopy.distance.geodesic(newStartPoint,locationPonits[i]).km
#             for j in range(len(visitedPointsList)):
#                 localRealCost+=geopy.distance.geodesic(newStartPoint,visitedPointsList[j]).km
#             localEstimationCost = geopy.distance.geodesic(newStartPoint,targetPoint).km
#             totalCost = localRealCost+localEstimationCost
#             totalCostList.append(totalCost)
#             newStartPointIndex =totalCostList.index(min(totalCostList))
#             visitedPointsList.append(newStartPoint)
#             if(newStartPointIndex>=len(locationPonits)):
#                 print('000000000')
#                 newStartPoint=targetPoint
#                 break
#             else:   
#                 print(newStartPointIndex)
#                 newStartPoint = locationPonits[newStartPointIndex]
                


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


 










