import time, math

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

rotations = {
    'clockwise': {
        (-1,-1): (-1,1),
        (-1,0): (-1,1),
        (-1,1): (1,1),
        (0,1): (1,1),
        (1,1): (1,-1),
        (1,0): (1,-1),
        (1,-1): (-1,-1),
        (0,-1): (-1,-1)
    },
    'counterClockwise': {
        (-1,-1): (1,-1),
        (-1,0): (-1,-1),
        (-1,1): (-1,-1),
        (0,1): (-1,1),
        (1,1): (-1,1),
        (1,0): (1,1),
        (1,-1): (1,1),
        (0,-1): (1,-1)
    }
}

rotationMapping = {
    'L': 'counterClockwise',
    'J': 'clockwise',
    '7': 'counterClockwise',
    'F': 'clockwise'
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

def getClosest(c, l, spaceCode):
    if spaceCode in rotationMapping:
        return rotations[rotationMapping[spaceCode]][c]
    minDist = 99
    minTup = None
    for d in l:
        dTup = directions[d]
        dist = math.dist(c,dTup)
        if dist <= 1.0:
            return dTup
            

def determineInnerArea(inside,outside):
    for n in visited:
        spaceCode = pipeMap[n[0]][n[1]]
        if spaceCode == 'S':
            continue
        inOut = inOutCodes[pipeMap[n[0]][n[1]]]
        inside = getClosest(inside, inOut, spaceCode)
        outside = getClosest(outside, inOut, spaceCode)
        print(n, spaceCode, inside, outside)
        innerSpot = (n[0]+inside[0],n[1]+inside[1])
        outerSpot = (n[0]+outside[0],n[1]+outside[1])
        if innerSpot not in visited:
            if innerSpot[0] >= 0 and innerSpot[0] < len(pipeMap) and innerSpot[1] >=0 and innerSpot[1] < len(pipeMap[innerSpot[0]]):
                pipeMap[innerSpot[0]][innerSpot[1]] = 'I'
        if outerSpot not in visited:
            if outerSpot[0] >= 0 and outerSpot[0] < len(pipeMap) and outerSpot[1] >=0 and outerSpot[1] < len(pipeMap[outerSpot[0]]):
                pipeMap[outerSpot[0]][outerSpot[1]] = 'O'

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
            if newCords[0] >= 0 and newCords[0] < len(pipeMap) and newCords[1] >=0 and newCords[1] < len(pipeMap[newCords[0]]) and not newCords in visited:
                if pipeMap[newCords[0]][newCords[1]] != 'I':
                    pipeMap[newCords[0]][newCords[1]] = 'I'
                    queue.append(newCords)
            

def main():
    with open('testInput5.txt') as f:
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
    print(inside,outside)
    determineInnerArea(inside, outside)

    #expandIs()

    cumSum = 0
    for pipe in pipeMap:
        print(''.join(pipe))
        cumSum+=pipe.count('I')

    return cumSum

if __name__ == '__main__':
    x = time.perf_counter_ns()
    answer = main()
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
