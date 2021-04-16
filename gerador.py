import json
from random import random


def generateRandomData(nStudents, maxWalk, nReachablePoints, minDistance, maxDistance):

    rp = [[minDistance + (maxDistance - minDistance) * random()
           for i in range(nStudents)] for j in range(nReachablePoints)]
    data = {
        'nStudents': nStudents,
        'rp': rp,
        'maxWalk': maxWalk
    }
    # print(rp[0])

    with open('data.json', 'w') as jsonF:
        json.dump(data, jsonF)


generateRandomData(1000, 100, 500, 0, 20000)
