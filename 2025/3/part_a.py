#!/usr/bin/env python3
import time, re
from aocd import data, submit

EXAMPLE_DATA='''987654321111111
811111111111119
234234234234278
818181911112111'''
EXAMPLE_ANSWER=357

def main(data):
    result = 0
    for bank in data.splitlines():
        max_a=0
        a_index=0
        for i,n in enumerate(str(bank)[:-1]):
            if int(n) > max_a:
                max_a = int(n)
                a_index=i
        max_b = int(max(str(bank)[a_index+1:]))
        result += (max_a * 10) + max_b
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
