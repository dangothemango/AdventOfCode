import time

def calcDiffs(nums):
    diffs = list()
    for i in range(len(nums)-1):
        diffs.append(nums[i+1]-nums[i])
    retDiffs = None
    if [x for x in diffs if x != 0]:
        retDiffs = calcDiffs(diffs)
    if not retDiffs:
        diffs.append(0)
        return diffs
    diffs.insert(0,diffs[0]-retDiffs[0])
    return diffs

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    ans = list()
    for line in lines:
        nums = line.strip().split(' ')
        for i in range(len(nums)):
            nums[i]=int(nums[i])
        result = calcDiffs(nums)
        ans.insert(0,nums[0]-result[0])
    return sum(ans)

if __name__ == '__main__':
    x = time.perf_counter_ns()
    answer = main()
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
