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
EXAMPLE_ANSWER=6

#ABS +1 = NZ->Z -1
#ABS -1 = Z->NZ -1

def main(data):
    start=50
    result=0
    for line in data.splitlines():
        dir=1 if line[0] == 'R' else -1
        dist=int(line[1:]) * dir
        new_pos=start + dist
        if start == 0 and new_pos%100 != 0 and dir == -1:
            result += abs(new_pos//100) - 1
        elif start != 0 and new_pos%100 == 0 and dir == -1:
            result += abs(new_pos//100) + 1
        else:
            result += abs(new_pos//100)
        print(result)
        start = new_pos%100
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
