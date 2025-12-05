#!/usr/bin/env python3
import time, re
from aocd import data, submit

EXAMPLE_DATA='''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''
EXAMPLE_ANSWER=3

def main(data):
    range_data, ids = data.split('\n\n')
    ranges = list()
    freshIngredients = 0
    for range in range_data.splitlines():
        start, end = range.split('-')
        ranges.append((int(start),int(end)))
    for id in ids.splitlines():
        id=int(id)
        for range in ranges:
            if id >= range[0] and id <= range[1]:
                freshIngredients+=1
                break
    return freshIngredients

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
