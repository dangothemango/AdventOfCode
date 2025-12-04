#!/usr/bin/env python3
import time, re
from aocd import data, submit

EXAMPLE_DATA='''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''
EXAMPLE_ANSWER=43

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

def isDirPaper(cords, direction, data):
    dirValue = directions[direction]
    newCords = (cords[0]+dirValue[0],cords[1]+dirValue[1])
    if newCords[0] >= 0 and newCords[0] < len(data) and newCords[1] >=0 and newCords[1] < len(data[newCords[0]]):
        return data[newCords[0]][newCords[1]] == '@'
    return False

def main(data):
    result=0
    splitData=data.splitlines()
    for i in range(len(splitData)):
        splitData[i] = list(splitData[i])
    oldResult = -1
    while result != oldResult:
        oldResult = result
        for y, line in enumerate(splitData):
            for x, thing in enumerate(line):
                if thing == '@':
                    count=0
                    for dir in directions:
                        if isDirPaper((y,x), dir, splitData):
                            count += 1
                            if count >= 4:
                                break
                    if count < 4:
                        result+=1
                        splitData[y][x] = '.'
    return result

if __name__ == '__main__':
    ex_answer=main(EXAMPLE_DATA)
    print('Example Answer:', ex_answer)
    assert ex_answer == EXAMPLE_ANSWER
    x = time.perf_counter_ns()
    answer = main(data)
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
    submit(answer)
