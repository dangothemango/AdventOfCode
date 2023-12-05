import time

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    return None

if __name__ == '__main__':
    x = time.perf_counter_ns()
    answer = main()
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000)
