import json
import random
from graficos import grafico_distancia, grafico_pontos


def getLC(nStudents, rp, maxWalk):

    lc = [[i, 0] for i in range(len(rp))]
    reachabilities = [[] for i in range(len(rp))]
    studentReachabilities = [[] for i in range(nStudents)]
    for i in range(len(rp)):
        for j in range(nStudents):
            if rp[i][j] < maxWalk:
                lc[i][1] += 1
                reachabilities[i].append(j)
                studentReachabilities[j].append(i)

    lc.sort(reverse=True, key=lambda x: x[1])
    return lc, reachabilities, studentReachabilities


def construct(nStudents, lc, reachabilities, studentReachabilities, alpha):

    attendedStudents = 0
    alreadyAttended = set()
    solution = []
    while attendedStudents < nStudents:
        lrc = []
        if len(lc) == 0:
            break
        minValue = lc[-1][1]
        maxValue = lc[0][1]
        for i in range(len(lc)):
            c = lc[i]
            if c[1] >= minValue + alpha * (maxValue - minValue):
                lrc.append(i)
        chosen = random.choice(lrc)
        for student in reachabilities[lc[chosen][0]]:
            if student in alreadyAttended:
                continue
            alreadyAttended.add(student)
            solution.append([student, lc[chosen][0]])
            attendedStudents += 1
        del lc[chosen]
        lc.sort(reverse=True, key=lambda x: x[1])

    if attendedStudents < nStudents:
        for n in range(nStudents):
            if n not in alreadyAttended:
                solution.append([n, 'house'])

    return solution


def numberOfBusStops(solution):
    bs = set()
    houses = 0
    for s in solution:
        if s[1] == 'house':
            houses += 1
        else:
            bs.add(s[1])
        
    counts = [0 for s in range(500)]
    for s in solution:
        if s[1] == 'house':
            houses += 1
        else:
            counts[s[1] % 500] += 1
    
    for c in counts:
        if c == 0:
            continue
    #     print(f'{c} in a bus stop')
    # print(f'{houses} in the house')
    return len(bs) + houses


def getDistance(rp, busStop, student):
    if busStop == 'house':
        return 0
    else:
        return rp[busStop][student]


def improve(solution, rp, maxWalk):
    cont = True
    while(cont):
        changed = False
        for i in range(len(solution)):
            s = solution[i]
            student = s[0]
            bs = s[1]
            for j in range(len(solution)):
                if i == j or solution[j][1] == 'house':
                    continue
                innerS = solution[j]
                innerBs = innerS[1]
                if bs == 'house':
                    if rp[innerBs][student] < maxWalk:
                        s[1] = innerBs
                        changed = True
                else:
                    if rp[innerBs][student] < rp[bs][student]:
                        s[1] = innerBs
                        changed = True
        cont = changed

def improveHouse(solution, rp, maxWalk):
    cont = True
    while(cont):
        changed = False
        for i in range(len(solution)):
            s = solution[i]
            student = s[0]
            bs = s[1]
            for j in range(len(solution)):
                if i == j or solution[j][1] == 'house':
                    continue
                innerS = solution[j]
                innerBs = innerS[1]
                if bs == 'house':
                    if rp[innerBs][student] < maxWalk:
                        s[1] = innerBs
                        changed = True
                else:
                    if rp[innerBs][student] < rp[bs][student]:
                        s[1] = innerBs
                        changed = True
        cont = changed

def improveReduceBusStops(solution, rp, maxWalk):
    busStops = set()
    busStopStudents = {}
    for c, s in enumerate(solution):
        if s[1] == 'house':
            continue
        busStops.add(s[1])
        if busStopStudents.get(s[1]):
            busStopStudents[s[1]].append([s[0], c])
        else:
            busStopStudents[s[1]] = [[s[0], c]]
    
    cont = True
    while(cont):
        changed = False
        toBeRemoved = set()
        for bs in busStops:
            for innerBs in busStops:
                if innerBs == bs or innerBs in toBeRemoved:
                    continue
                allReaches = True
                # print(busStopStudents.keys())
                # print(busStops)
                for student in busStopStudents[bs]:
                    if rp[innerBs][student[0]] > maxWalk:
                        allReaches = False
                        break
                if allReaches:
                    for entry in busStopStudents[bs]:
                        # print(entry)
                        # print(s[entry[1]])
                        # print(len(s))
                        solution[entry[1]][1] = innerBs
                        busStopStudents[innerBs].append([solution[entry[1]][0], entry[1]])
                    toBeRemoved.add(bs)
                    changed = True
        for bs in toBeRemoved:
            busStops.remove(bs)
            del busStopStudents[bs]
        # code goes here
        cont = changed


def walkMean(rp, solution):
    mean = 0
    for s in solution:
        mean += rp[s[1]][s[0]] if s[1] != 'house' else 0
    return mean / len(solution)


def grasp(alpha, nIter, nomeGraficoDistancia, nomeGraficoPontos):
    data = {}

    with open('data.json', 'r') as jsonF:
        data = json.loads(jsonF.read())

    nStudents = data['nStudents']
    maxWalk = data['maxWalk']
    rp = data['rp']

    # print(lc)
    # print(reachabilities)
    historic = []
    best = None
    for counter in range(nIter):
        lc, reachabilities, studentReachabilities = getLC(
            nStudents, rp, maxWalk)
        for s in reachabilities[0]:
            if rp[0][s] > maxWalk:
                print(f'Invalid: {rp[0][s]}')
        # break
        solution = construct(nStudents, lc, reachabilities,
                             studentReachabilities, alpha)
        # print(solution)
        # print(len(solution))
        # print(numberOfBusStops(solution))
        # print(walkMean(rp, solution))
        # improve(solution, rp, maxWalk)
        improveReduceBusStops(solution, rp, maxWalk)
        improve(solution, rp, maxWalk)
        improveReduceBusStops(solution, rp, maxWalk)
        # print(solution)
        # print(numberOfBusStops(solution))
        # print(walkMean(rp, solution))
        if counter == 0:
            best = solution
        else:
            solutionBs = numberOfBusStops(solution)
            bestBs = numberOfBusStops(best)
            if solutionBs < bestBs:
                best = solution
            elif solutionBs == bestBs:
                if walkMean(rp, solution) < walkMean(rp, best):
                    best = solution
        historic.append(best)
        print(f'Finished iteration {counter + 1} with best of {numberOfBusStops(best)} and avg walk {walkMean(rp, best)}.')
    print(f'Best: {numberOfBusStops(best)} with avg walk {walkMean(rp, best)}')
    grafico_distancia([i for i in range(nIter)], [walkMean(rp, s) for s in historic], nomeGraficoDistancia)
    grafico_pontos([i for i in range(nIter)], [numberOfBusStops(s) for s in historic], nomeGraficoPontos)

grasp(1, 15, 'distancia1', 'pontos1')
grasp(0.5, 15, 'distancia05', 'pontos05')
grasp(0, 15, 'distancia0', 'pontos0')