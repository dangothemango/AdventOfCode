import time

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        lines[i] = list(line.strip())

    cumSum = 0
    
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == 'O':
                k = i-1
                while k>=0 and lines[k][j]=='.':
                    k-=1
                line[j] = '.'
                lines[k+1][j] = 'O'
                cumSum+=len(lines)-(k+1)

    return cumSum

if __name__ == '__main__':
    x = time.perf_counter_ns()
    answer = main()
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
