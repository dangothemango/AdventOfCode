#!/usr/bin/env python3
import time, re
from aocd import data, submit

EXAMPLE_DATA='''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''
EXAMPLE_ANSWER=3

def main(data):
    start=50
    result=0
    for line in data.splitlines():
        dir=1 if line[0] == 'R' else -1
        dist=int(line[1:]) * dir
        start+=dist
        start=start%100
        if not start:
            result+=1
    print(result)
    return result

if __name__ == '__main__':
    assert main(EXAMPLE_DATA) == EXAMPLE_ANSWER
    x = time.perf_counter_ns()
    answer = main(data)
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
    submit(answer)
