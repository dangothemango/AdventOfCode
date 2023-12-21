import time, math, sys
from queue import PriorityQueue

directions = {
    (-1,0),
    (0,1),
    (1,0),
    (0,-1),
}

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        lines[i] = line.strip()

    searchQueue = PriorityQueue()
    searchQueue.put((0, (0,0), (0,0), [], []))
    visited = {
        str((0,0)): {
            str([]): 0
        }
    }
    while not searchQueue.empty():
        current = searchQueue.get()
        point = current[1]
        restrictedDirections = [(-current[2][0],-current[2][1])]
        if len(current[3]) == 3 and len(set(current[3])) == 1:
            restrictedDirections.append(current[3][0])
        for dir in directions.difference(set(restrictedDirections)):
            newPoint = (point[0]+dir[0],point[1]+dir[1])
            if newPoint[0] < 0 or newPoint[0] >= len(lines) or newPoint[1] < 0 or newPoint[1] >= len(lines[newPoint[0]]):
                continue
            heat = int(lines[newPoint[0]][newPoint[1]]) + current[0]
            pointStr = str(newPoint)
            newDirs = current[3][-2:]+[dir]
            dirStr = str(newDirs)
            if pointStr in visited and dirStr in visited[pointStr] and visited[pointStr][dirStr] <= heat:
                continue
            if pointStr not in visited:
                visited[pointStr] = dict()
            visited[pointStr][dirStr] = heat
            searchQueue.put((heat, newPoint, dir, newDirs, dirStr))


    #print(visited)
    print(visited[str((len(lines)-1,len(lines)-1))])
    return min(visited[str((len(lines)-1,len(lines)-1))].values())
    return minDist

if __name__ == '__main__':
    x = time.perf_counter_ns()
    answer = main()
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
