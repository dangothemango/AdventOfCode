#!/usr/bin/env python3
import time, re
from aocd import data, submit

EXAMPLE_DATA='''.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............'''
EXAMPLE_ANSWER=40

memos = {}

def recursionHelper(data, loc):
    newLoc = loc
    while newLoc[0]< len(data) and data[newLoc[0]][newLoc[1]] == '.':
        newLoc=(newLoc[0]+1, newLoc[1])
    if newLoc[0] == len(data):
        return 1
    if newLoc in memos:
        return memos[newLoc]
    result = recursionHelper(data, (newLoc[0], newLoc[1]-1)) + recursionHelper(data, (newLoc[0], newLoc[1]+1))
    memos[newLoc] = result
    return result

def main(data):
    data = data.splitlines()
    loc = (1, data[0].find('S'))
    return recursionHelper(data, loc)

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
