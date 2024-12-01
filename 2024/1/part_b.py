import time, aocd, re

EXAMPLE_DATA='''3   4
4   3
2   5
1   3
3   9
3   3'''
EXAMPLE_ANSWER=31

def get_data():
    return aocd.get_data()

def main(data):
    A,B=list(),dict()
    #Parse list
    for line in data.split('\n'):
        nums=re.split(r'\s+', line)
        A.append(int(nums[0]))
        bNum=int(nums[1])
        if bNum not in B:
            B[bNum] = 0
        B[bNum]+=1
    A.sort()
    simScore=0
    for i in A:
        simScore+=i * (B[i] if i in B else 0)
    return simScore

if __name__ == '__main__':
    assert main(EXAMPLE_DATA) == EXAMPLE_ANSWER
    data = get_data()
    x = time.perf_counter_ns()
    answer = main(data)
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
    aocd.submit(answer)
