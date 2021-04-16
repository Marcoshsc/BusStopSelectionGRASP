import json
from random import random


def generateRandomData(nStudents, maxWalk, nReachablePoints, minDistance, maxDistance):

    rp = [[minDistance + (maxDistance - minDistance) * random()
           for i in range(nStudents)] for j in range(nReachablePoints)]
    for r in rp:
        r.append(maxWalk)
    data = {
        'nStudents': nStudents,
        'rp': rp,
        'maxWalk': maxWalk
    }

    with open('data.json', 'w') as jsonF:
        json.dump(data, jsonF)


generateRandomData(1000, 400, 100, 0, 3000)
