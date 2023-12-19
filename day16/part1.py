import time

directions = {
    'north': (-1,0),
    'east': (0,1),
    'south': (1,0),
    'west': (0,-1),
}

mirrorCodes = {
    '.': {
        'north': ['north'],
        'east': ['east'],
        'south': ['south'],
        'west': ['west']
    },
    '-': {
        'north': ['east', 'west'],
        'east': ['east'],
        'south': ['east', 'west'],
        'west': ['west']
    },
    '|': {
        'north': ['north'],
        'east': ['north', 'south'],
        'south': ['south'],
        'west': ['north','south']
    },
    '\\': {
        'north': ['west'],
        'east': ['south'],
        'south': ['east'],
        'west': ['north']
    },
    '/': {
        'north': ['east'],
        'east': ['north'],
        'south': ['west'],
        'west': ['south']
    }
}

def getHeat(startingPoint, lines):
    points = [startingPoint]
    visited = {
        str(points[0][0]):{points[0][1]}
    }
    while len(points) > 0:
        pointDir = points.pop()
        direction = pointDir[1]
        point = pointDir[0]
        char = lines[point[0]][point[1]]
        for dir in mirrorCodes[char][direction]:
            newPoint = (point[0] + directions[dir][0],point[1]+directions[dir][1])
            if newPoint[0] >= 0 and newPoint[0] < len(lines) and newPoint[1] >= 0 and newPoint[1] < len(lines[newPoint[0]]):
                label = str(newPoint)
                if label not in visited:
                    visited[label] = set()
                if dir not in visited[label]:
                    visited[label].add(dir)
                    points.append((newPoint, dir))
    return len(visited)

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        lines[i] = line.strip()

    return getHeat(((0,0),'east'), lines)

if __name__ == '__main__':
    x = time.perf_counter_ns()
    answer = main()
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
