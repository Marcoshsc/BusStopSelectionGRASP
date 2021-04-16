from haversine import haversine, Unit
from random import random
import json

def getRandomCoord(minLon, maxLon, minLat, maxLat):
    lon = minLon + (maxLon - minLon) * random()
    lat = minLat + (maxLat - minLat) * random()
    return (lat, lon)


def generateRandomData(nStudents, maxWalk, nReachablePoints, bound):

    minLat = bound['minLat']
    maxLat = bound['maxLat']
    minLon = bound['minLon']
    maxLon = bound['maxLon']
    
    studentPoints = [getRandomCoord(minLon, maxLon, minLat, maxLat) for i in range(nStudents)]
    reachablePoints = [getRandomCoord(minLon, maxLon, minLat, maxLat) for i in range(nReachablePoints)]
    rp = [[haversine(studentPoints[i], reachablePoints[j], Unit.METERS) for i in range(nStudents)] for j in range(nReachablePoints)]
    data = {
        'nStudents': nStudents,
        'rp': rp,
        'maxWalk': maxWalk
    }
    # print(rp[0])

    with open('data.json', 'w') as jsonF:
        json.dump(data, jsonF)

generateRandomData(1000, 1000, 100, {
    'minLat': -19.969477,
    'minLon': -43.976898,
    'maxLat': -19.896534,
    'maxLon': -43.903427
})
# loc1=(28.426846,77.088834)
# loc2=(28.394231,77.050308)
# print(haversine(loc1,loc2, unit=Unit.METERS))