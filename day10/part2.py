import time, math

#This is not good or complete but I was able to use it to get a correct answer

directions = {
    'north': (-1,0),
    'northEast': (-1,1),
    'east': (0,1),
    'southEast': (1,1),
    'south': (1,0),
    'southWest': (1,-1),
    'west': (0,-1),
    'northWest': (-1,-1)
}

codes = {
    '|': ['north', 'south'],
    '-': ['east', 'west'],
    'L': ['north', 'east'],
    'J': ['north', 'west'],
    '7': ['south', 'west'],
    'F': ['south','east'],
    'S': ['north','west','south','east'],
    'I': ['north','west','south','east'],
    'O': ['north','west','south','east'],
    '.': []
}

inOutCodes = {
    '|': ['west', 'east'],
    '-': ['north', 'south'],
    'L': ['northEast', 'southWest'],
    'J': ['northWest', 'southEast'],
    '7': ['southWest', 'northEast'],
    'F': ['southEast','northWest']
}

rotationMapping = {
    'F': {
        directions['north']: 1,
        directions['west']: -1
    },
    'J': {
        directions['south']: 1,
        directions['east']: -1
    },
    'L': {
        directions['south']: -1,
        directions['west']: 1
    }
    ,
    '7': {
        directions['north']: -1,
        directions['east']: 1
    }
}

def getPipeInDirection(cords, direction):
    dirValue = directions[direction]
    newCords = (cords[0]+dirValue[0],cords[1]+dirValue[1])
    pipe = None
    if newCords[0] >= 0 and newCords[0] < len(pipeMap) and newCords[1] >=0 and newCords[1] < len(pipeMap[newCords[0]]):
        pipe = pipeMap[newCords[0]][newCords[1]]
    return pipe, newCords

def getConnectedTiles(cord):
    code = pipeMap[cord[0]][cord[1]]
    tiles = dict()
    for direction in codes[code]:
        code,loc = getPipeInDirection(cord, direction)
        if code != None:
            tiles[loc] = code
    return tiles

pipeMap = list()
visited = dict()

def moveThroughPipe(rCord, depth):
    while rCord:
        visited[rCord] = depth
        rConnected = getConnectedTiles(rCord)
        rNext = None
        for c in rConnected:
            if c in visited:
                continue
            else:
                rNext = c
        depth += 1
        rCord = rNext

def getClosest(c, l, spaceCode, prevCode, movementDirection, prevMovementDirection):
    minDist = 99
    minTup = None
    if spaceCode in rotationMapping and prevCode in rotationMapping:
        for i, d in enumerate(inOutCodes[prevCode]):
            if directions[d] == c:
                print(prevCode,spaceCode,inOutCodes[prevCode],c,l,inOutCodes[spaceCode][i])
                new = i if rotationMapping[spaceCode][movementDirection] == rotationMapping[prevCode][prevMovementDirection] else (i+1)%2
                return (directions[inOutCodes[spaceCode][new]])
    for d in l:
        dTup = directions[d]
        dist = math.dist(c,dTup)
        if dist <= 1.0:
            return dTup

            

def determineInnerArea(inside,outside, sCords):
    prevSpaceCode = '7'
    prevMovementDirection = directions['west']
    prevCords = sCords
    for n in visited:
        spaceCode = pipeMap[n[0]][n[1]]
        if spaceCode == 'S':
            continue
        movementDirection = (n[0]-prevCords[0], n[1]-prevCords[1])
        print(movementDirection)
        inOut = inOutCodes[pipeMap[n[0]][n[1]]]
        inside = getClosest(inside, inOut, spaceCode, prevSpaceCode, movementDirection, prevMovementDirection)
        outside = getClosest(outside, inOut, spaceCode, prevSpaceCode, movementDirection, prevMovementDirection)
        innerSpot = (n[0]+inside[0],n[1]+inside[1])
        outerSpot = (n[0]+outside[0],n[1]+outside[1])
        if innerSpot not in visited:
            if innerSpot[0] >= 0 and innerSpot[0] < len(pipeMap) and innerSpot[1] >=0 and innerSpot[1] < len(pipeMap[innerSpot[0]]):
                pipeMap[innerSpot[0]][innerSpot[1]] = 'O'
        if outerSpot not in visited:
            if outerSpot[0] >= 0 and outerSpot[0] < len(pipeMap) and outerSpot[1] >=0 and outerSpot[1] < len(pipeMap[outerSpot[0]]):
                pipeMap[outerSpot[0]][outerSpot[1]] = 'I'
        prevSpaceCode = spaceCode
        prevCords = n 
        prevMovementDirection = movementDirection

def expandIs():
    queue = list()
    for i, line in enumerate(pipeMap):
        for j, c in enumerate(line):
            if c == 'I':
                queue.append((i,j))
    while len(queue) > 0:
        iLoc = queue.pop()
        for d in codes['I']:
            dirValue = directions[d]
            newCords = (iLoc[0]+dirValue[0],iLoc[1]+dirValue[1])
            if newCords[0] >= 0 and newCords[0] < len(pipeMap) and newCords[1] >=0 and newCords[1] < len(pipeMap[newCords[0]]) and newCords not in visited:
                if pipeMap[newCords[0]][newCords[1]] != 'I':
                    pipeMap[newCords[0]][newCords[1]] = 'I'
                    queue.append(newCords)

def expandOs():
    queue = list()
    for i, line in enumerate(pipeMap):
        for j, c in enumerate(line):
            if c == 'O':
                queue.append((i,j))
    while len(queue) > 0:
        iLoc = queue.pop()
        for d in codes['O']:
            dirValue = directions[d]
            newCords = (iLoc[0]+dirValue[0],iLoc[1]+dirValue[1])
            if newCords[0] >= 0 and newCords[0] < len(pipeMap) and newCords[1] >=0 and newCords[1] < len(pipeMap[newCords[0]]) and newCords not in visited:
                if pipeMap[newCords[0]][newCords[1]] != 'O':
                    pipeMap[newCords[0]][newCords[1]] = 'O'
                    queue.append(newCords)
            

def main():
    with open('input.txt') as f:
        lines = f.readlines()
    
    for line in lines:
        pipeMap.append(list(line.strip()))
    
    sCords = (0,0)
    for i, line in enumerate(pipeMap):
        for j, c in enumerate(line):
            if c == 'S':
                sCords = (i,j)

    sConnects = getConnectedTiles(sCords)
    connectedToS = list()
    visited[sCords] = 0
    for c in sConnects.keys():
        tiles = getConnectedTiles(c)
        if 'S' in tiles.values():
            connectedToS.append(c)
    print(sCords, connectedToS[0])
    moveThroughPipe(connectedToS[0], 1)
    # print(visited)
    y = sCords[0]
    x = sCords[1]
    for c in connectedToS:
        if c[0] != sCords[0]:
            y = c[0]
        if c[1] != sCords[1]:
            x = c[1]
    inside = ((y-sCords[0],x-sCords[1]))
    outside = (inside[0]*-1, inside[1]*-1)
    determineInnerArea(inside, outside, sCords)
    
    expandIs()
    expandOs()

    for i,pipe in enumerate(pipeMap):
        for j,code in enumerate(pipeMap[i]):
            if (i,j) not in visited and pipeMap[i][j] not in ['I','O']:
                pipeMap[i][j] = '.'
            

    cumSum = 0
    for pipe in pipeMap:
        print(''.join(pipe).replace('L','⌎').replace('F','⌌').replace('J','⌏').replace('7','⌍'))
        cumSum+=pipe.count('I')


    return cumSum

if __name__ == '__main__':
    x = time.perf_counter_ns()
    answer = main()
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
