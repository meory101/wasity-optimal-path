import geopy
from geopy import distance
# my work location 
distance =[]
firstPoint = (33.51565,36.26555)

items = [(33.54342,36.24455),(33.1011,36.099),
         (33.777,36.8888) ]


def CalculateCost(firstNode,secondNode):
    return geopy.distance.geodesic(firstNode,secondNode).km


for i in range(len(items)):
    distance.append(CalculateCost(firstNode=firstPoint,secondNode=items[i]))