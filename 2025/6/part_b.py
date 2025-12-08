#!/usr/bin/env python3
import time, re
from aocd import data, submit

EXAMPLE_DATA='''123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  '''
EXAMPLE_ANSWER=3263827

def main(data):
    data = data.splitlines()
    operator=None
    result = 0
    nums=list()
    for i in range(len(data[0])):
        if not operator:
            operator=data[-1][i]
        if set([x[i] for x in data[:-1]]) == set(' '):
            #todo evaluate math
            result+=eval(operator.join(nums))
            operator = None
            nums.clear()
        else:   
            nums.append(''.join([x[i] for x in data[:-1] if x[i] != ' ']))
    result+=eval(operator.join(nums))
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
