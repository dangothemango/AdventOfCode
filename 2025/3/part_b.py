#!/usr/bin/env python3
import time, re
from aocd import data, submit

EXAMPLE_DATA='''987654321111111
811111111111119
234234234234278
818181911112111'''
EXAMPLE_ANSWER=3121910778619


# skippable = 3
# iterate index 0 - 3
# 987654321111111
# max = 0
# skippable = 3
# iterate 1 to 4
# ....
# skippable == remaining + 1 
# max(12 to 15)

# 234234234234278
# iterate index 0 - 3
# 4
# two skipped
# skippable = 1
# iterate 4 to 5
# 3
# skippable = 0

def main(data):
    result = 0
    for bank in data.splitlines():
        index = 0
        skippable = len(bank) - 12
        num = list()
        while skippable > 0 and len(num) < 12:
            m = 0
            ind = 0
            for i, n in enumerate(bank[index:index+skippable+1]):
                if int(n) > m:
                    m = int(n)
                    ind = i
            num.append(str(m))
            index+=ind+1
            skippable-=ind
        if skippable == 0 and len(num) < 12:
            for i in bank[index:]:
                num.append(str(i))
        result+=int(''.join(num))
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
