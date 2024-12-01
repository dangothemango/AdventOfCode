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

    location = (0,0)
    map = [['#']]
    for line in lines:
        data = line.strip(')\n').split(' (')
        drillCommand = data[0]
        color = data[1]
        dir, distance = drillCommand.split(' ')
        for i in range(int(distance)):
            location = (location[0]+directions[dir][0], location[1]+directions[dir][1])
            if location[0] < 0:
                map.insert(0,['.']*len(map[0]))
                location = (location[0]+1, location[1])
            elif location[0] >= len(map):
                map.append(['.']*len(map[0]))
            elif location[1] < 0:
                for row in map:
                    row.insert(0,'.')
                location = (location[0], location[1]+1)
            elif location[1] >= len(map[0]):
                for row in map:
                    row.append('.')
            map[location[0]][location[1]] = '#'
    for row in map:
        print(''.join(row))

    map[0][0] = 'O'
    map[0][350] = 'O'
    map[len(map)-1][0] = 'O'
    map[len(map)-1][350] = 'O'
    map[198][350] = 'O'
    map[len(map)-1][215] = 'O'
    queue = [(0,0),(0,350),(len(map)-1,0),(len(map)-1,350),(len(map)-1,215),(198,350)]
    while len(queue) > 0:
        iLoc = queue.pop()
        for d in directions:
            dirValue = directions[d]
            newCords = (iLoc[0]+dirValue[0],iLoc[1]+dirValue[1])
            if newCords[0] >= 0 and newCords[0] < len(map) and newCords[1] >=0 and newCords[1] < len(map[newCords[0]]):
                if map[newCords[0]][newCords[1]] not in ['O','#']:
                    map[newCords[0]][newCords[1]] = 'O'
                    queue.append(newCords)

    for row in map:
        print(''.join(row))

    cumSum = 0 
    for line in map:
        cumSum+= line.count('#') + line.count('.')

    return cumSum

if __name__ == '__main__':
    x = time.perf_counter_ns()
    answer = main()
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
