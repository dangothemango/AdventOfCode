#!/usr/bin/env python3
import time, re
from aocd import data, submit

EXAMPLE_DATA='''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'''
EXAMPLE_ANSWER=4174379265

def main(data):
    result = 0
    for r in data.split(','):
        ends=r.split('-')
        for i in range(int(ends[0]),int(ends[1])+1):
            str_i = str(i)
            for term in range(0,len(str_i)//2):
                pat = str_i[0:term+1]
                if len(str_i)%len(pat) != 0:
                    continue
                mult=1
                while (mult+1) * len(pat) <= len(str_i):
                    if str_i[len(pat)*mult:len(pat)*mult+len(pat)] != pat:
                        break
                    mult+=1
                else:
                    result+=i
                    break
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
