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
EXAMPLE_ANSWER=21

def main(data):
    data = data.splitlines()
    data[0] = data[0].replace('S', '|')
    data = [list(x) for x in data]
    splits = 0
    for i in range(1, len(data)):
        for j in range(len(data[i])):
            if data[i-1][j] == '|':
                if data[i][j] == '^':
                    if j >0:
                        data[i][j-1] = '|'
                    if j < len(data[i])-1:
                        data[i][j+1] = '|'
                    splits+=1
                else:
                    data[i][j] = '|'
    return splits



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
