import time

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        lines[i] = list(line.strip())

    foundCycle = False
    ends = dict()
    cycle = 0
    numCycles = 1000000000
    while cycle < numCycles:
        #north
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                if c == 'O':
                    k = i-1
                    while k>=0 and lines[k][j]=='.':
                        k-=1
                    line[j] = '.'
                    lines[k+1][j] = 'O'
                
        #west
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                if c == 'O':
                    k = j-1
                    while k>=0 and lines[i][k]=='.':
                        k-=1
                    line[j] = '.'
                    lines[i][k+1] = 'O'
                    
        #south
        for i, line in enumerate(reversed(lines)):
            i = len(lines) - i - 1
            for j, c in enumerate(line):
                if c == 'O':
                    k = i+1
                    while k<len(lines) and lines[k][j]=='.':
                        k+=1
                    line[j] = '.'
                    lines[k-1][j] = 'O'
                
        #east
        for i, line in enumerate(lines):
            for j, c in enumerate(reversed(line)):
                j = len(line) - j - 1
                if c == 'O':
                    k = j+1
                    while k<len(line) and lines[i][k]=='.':
                        k+=1
                    line[j] = '.'
                    lines[i][k-1] = 'O'

        cycle += 1
        if not foundCycle and str(lines) in ends:
            diff = cycle - ends[str(lines)]
            cycle = (((numCycles - cycle) // diff) * diff) + cycle
            foundCycle = True
            
            print(ends[str(lines)])
        elif not foundCycle:
            ends[str(lines)] = cycle

    cumSum = 0           
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == 'O':
                cumSum+=len(lines)-i

    return cumSum

if __name__ == '__main__':
    x = time.perf_counter_ns()
    answer = main()
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
