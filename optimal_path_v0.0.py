import itertools

import geopy
import geopy.distance

locationPonitsNames=["mazzeh", "aspu", "marabaa","barada"]
locationPonits = [
    #mazzeh aspu marabaa barada
    (33.50496963350299, 36.26174203924571), 
    (33.600681416134506, 36.329047202425656),
    (33.57698377737123, 36.28683948478614),   
    (33.62751978497324, 36.10575190558477)    
]

allPossiblities = list(itertools.permutations(locationPonits))
allPossiblities = allPossiblities[:3]
# print("\n All Possible Paths From Delivery Location",  allPossiblities)
# print("\n All Possible Paths length",len(allPossiblities))

pathCostList = []
for i in range(len(allPossiblities)):
    print(allPossiblities[i])
    pathCost = 0
    for j in range(len(allPossiblities[i])-1):
            pathCost+= geopy.distance.geodesic(allPossiblities[i][j],allPossiblities[i][j+1]).km
    pathCostList.append(pathCost)



minPathCost = min(pathCostList)
minPathCostIndex = pathCostList.index(min(pathCostList))
bestPath = allPossiblities[minPathCostIndex]


print("App Baths Cost" ,pathCostList)
print("min cost" , minPathCost)
print("min cost index" , minPathCostIndex)
print("Best Path" ,bestPath )


for index in range(len(bestPath)):
      print(index, locationPonitsNames[bestPath.index(bestPath[index])])







