import time

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    starMap = list()
    # expand columns
    for line in lines:
        starMap.append(list(line.strip()))
        if len([x for x in line.strip() if x != '.']) == 0:
            starMap.append(list(line.strip()))
    columnsToAdd = list()
    for i in range(len(starMap[0])):
        empty = True
        for j in range(len(starMap)):
            if starMap[j][i] != '.':
                empty = False
                break
        if empty:
            columnsToAdd.append(i)
    for i in range(len(columnsToAdd)-1, -1, -1):
        for row in starMap:
            row.insert(columnsToAdd[i],'.')
    galaxies = set()
    for i, row in enumerate(starMap):
        for j, char in enumerate(row):
            if char == '#':
                galaxies.add((i,j))
    cumSum = 0
    while len(galaxies) > 0:
        start = galaxies.pop()
        for end in galaxies:
            cumSum += abs(end[0]-start[0]) + abs(end[1]-start[1])
    galaxiesUnexpanded = set()
    for i, row in enumerate(lines):
        for j, char in enumerate(row):
            if char == '#':
                galaxiesUnexpanded.add((i,j))
    cumSumUnexpanded = 0
    while len(galaxiesUnexpanded) > 0:
        start = galaxiesUnexpanded.pop()
        for end in galaxiesUnexpanded:
            cumSumUnexpanded += abs(end[0]-start[0]) + abs(end[1]-start[1])

    diff = 1000000
    return(cumSum - cumSumUnexpanded) * (diff-1) + cumSumUnexpanded

if __name__ == '__main__':
    x = time.perf_counter_ns()
    answer = main()
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
