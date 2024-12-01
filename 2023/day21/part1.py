import time

directions = {
    'U': (-1,0),
    'R': (0,1),
    'D': (1,0),
    'L': (0,-1),
}

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    map = list()
    startLoc = (-1,-1)
    for i, line in enumerate(lines):
        map.append(line.strip())
        if 'S' in line:
            startLoc = (i, line.index('S'))
    
    numSteps = 64
    locs = {str(startLoc)}
    for i in range(numSteps):
        newLocs = set()
        for locStr in locs:
            loc = eval(locStr)
            for dir in directions.values():
                newCords = (loc[0]+dir[0],loc[1]+dir[1])
                if newCords[0] >= 0 and newCords[0] < len(map) and newCords[1] >=0 and newCords[1] < len(map[newCords[0]]):
                    if (map[newCords[0]][newCords[1]]) != '#':
                        newLocs.add(str(newCords))
        locs = newLocs

    return len(locs)

if __name__ == '__main__':
    x = time.perf_counter_ns()
    answer = main()
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
