import time, re
from aocd import data, submit

EXAMPLE_DATA='''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''
EXAMPLE_ANSWER=2

def main(data):
    safe=0
    for line in data.split('\n'):
        nums = [int(x) for x in line.split(' ')]
        sortedNums=list(nums)
        sortedNums.sort()
        reversedNums = list(nums)
        reversedNums.reverse()
        if sortedNums != nums and sortedNums != reversedNums:
            continue
        isSafe=True
        for i in range(1,len(nums)):
            diff=nums[i]-nums[i-1]
            if abs(diff) < 1 or abs(diff) > 3:
                isSafe=False
                break
        safe+=(1 if isSafe else 0)
    return safe

if __name__ == '__main__':
    assert main(EXAMPLE_DATA) == EXAMPLE_ANSWER
    print(data)
    x = time.perf_counter_ns()
    answer = main(data)
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
    submit(answer)
