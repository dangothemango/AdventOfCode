import time, sys
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
    searchQueue.put((0, (0,0), (0,0), []))
    visited = {
        str((0,0)): {
            str([]): 0
        }
    }
    while not searchQueue.empty():
        current = searchQueue.get()
        point = current[1]
        restrictedDirections = list()
        if len(current[3]) == 0:
            pass
        elif len(current[3][-4:]) < 4 or len(set(current[3][-4:])) > 1:
            restrictedDirections = list(directions.difference(set(current[3][-1:])))
            if len(restrictedDirections) == 4:
                restrictedDirections = {}
        elif len(current[3]) == 10 and len(set(current[3])) == 1:
            restrictedDirections = [(-current[2][0],-current[2][1])]
            restrictedDirections.append(current[3][0])
        else:
            restrictedDirections = [(-current[2][0],-current[2][1])]
        for dir in directions.difference(set(restrictedDirections)):
            newPoint = (point[0]+dir[0],point[1]+dir[1])
            if newPoint[0] < 0 or newPoint[0] >= len(lines) or newPoint[1] < 0 or newPoint[1] >= len(lines[newPoint[0]]):
                continue
            heat = int(lines[newPoint[0]][newPoint[1]]) + current[0]
            pointStr = str(newPoint)
            newDirs = current[3][-9:]+[dir]
            dirStr = str(newDirs)
            if pointStr in visited and dirStr in visited[pointStr] and visited[pointStr][dirStr] <= heat:
                continue
            if pointStr not in visited:
                visited[pointStr] = dict()
            visited[pointStr][dirStr] = heat
            searchQueue.put((heat, newPoint, dir, newDirs))


    #print(visited)
    minDist = sys.maxsize
    for path in visited[str((len(lines)-1,len(lines[-1])-1))]:
        if len(set(eval(path)[-4:])) == 1:
               minDist = min(minDist, visited[str((len(lines)-1,len(lines[-1])-1))][path])

    return minDist

if __name__ == '__main__':
    x = time.perf_counter_ns()
    answer = main()
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
