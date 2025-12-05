#!/usr/bin/env python3
import time, re
from aocd import data, submit

EXAMPLE_DATA='''3-5
10-14
16-20
12-18
3-4
3-3
3-5

1
5
8
11
17
32'''
EXAMPLE_ANSWER=14

def main(data):
    range_data, _ = data.split('\n\n')
    ranges = list()
    for range in range_data.splitlines():
        start, end = range.split('-')
        ranges.append((int(start),int(end)))
    ranges.sort()
    i=0
    while i < len(ranges)-1:
        range=ranges[i]
        start, end=range
        if end >= ranges[i+1][0]:
            ranges[i]=(start,max(end,ranges[i+1][1]))
            ranges.pop(i+1)
            i-=1
        i+=1
    freshIngredients = 0
    for range in ranges:
        freshIngredients+=range[1]-range[0]+1

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
