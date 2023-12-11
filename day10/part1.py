import time

directions = {
    'north': (-1,0),
    'east': (0,1),
    'south': (1,0),
    'west': (0,-1),
}

codes = {
    '|': ['north', 'south'],
    '-': ['east', 'west'],
    'L': ['north', 'east'],
    'J': ['north', 'west'],
    '7': ['south', 'west'],
    'F': ['south','east'],
    'S': ['north','west','south','east'],
    '.': []
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

def moveThroughPipe(lCord,rCord, depth):
    while lCord and rCord:
        visited[lCord] = depth
        if (lCord == rCord):
            return
        visited[rCord] = depth
        lConnected = getConnectedTiles(lCord)
        lNext = None
        for c in lConnected:
            if c in visited:
                continue
            else:
                lNext = c
        rConnected = getConnectedTiles(rCord)
        rNext = None
        for c in rConnected:
            if c in visited:
                continue
            else:
                rNext = c
        depth += 1
        lCord, rCord = lNext, rNext

def main():
    with open('input.txt') as f:
        lines = f.readlines()
    
    for line in lines:
        pipeMap.append(line.strip())
    
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
    moveThroughPipe(connectedToS[0],connectedToS[1], 1)
    
    return max(visited.values())

if __name__ == '__main__':
    x = time.perf_counter_ns()
    answer = main()
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
