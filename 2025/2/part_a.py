#!/usr/bin/env python3
import time, re
from aocd import data, submit

EXAMPLE_DATA='''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'''
EXAMPLE_ANSWER=1227775554

def main(data):
    result = 0
    for r in data.split(','):
        ends=r.split('-')
        for i in range(int(ends[0]),int(ends[1])+1):
            str_i = str(i)
            l = len(str(i))
            if l%2 == 1:
                continue
            if str_i[0:l//2] == str_i[l//2:]:
                result += i
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
