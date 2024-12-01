import time, aocd, re

EXAMPLE_DATA='''3   4
4   3
2   5
1   3
3   9
3   3'''
EXAMPLE_ANSWER=11

def get_data():
    return aocd.get_data()

def main(data):
    return None

if __name__ == '__main__':
    assert main(EXAMPLE_DATA) == EXAMPLE_ANSWER
    data = get_data()
    x = time.perf_counter_ns()
    answer = main(data)
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
    aocd.submit(answer)
