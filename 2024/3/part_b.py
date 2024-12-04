import time, re
from aocd import data, submit

EXAMPLE_DATA='''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''
EXAMPLE_ANSWER=48

def main(data):
    sum=0
    enabled=True
    for mul in re.findall("(do(?:n't)?\(\)|mul\(\d+,\d+\))",data):
        if mul.startswith('d'):
            enabled=mul=='do()'
            continue
        if not enabled:
            continue
        nums = re.findall('\d+',mul)
        sum+=int(nums[0])*int(nums[1])
    return sum

if __name__ == '__main__':
    assert main(EXAMPLE_DATA) == EXAMPLE_ANSWER
    print(data)
    x = time.perf_counter_ns()
    answer = main(data)
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
    submit(answer)
