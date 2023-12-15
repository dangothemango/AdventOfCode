import time

def verticalReflection(m):
    return horizontalReflection(list(zip(*m)))

def checkDiffs(l1,l2):
    diffs = 0
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            diffs += 1
    return diffs

def horizontalReflection(m):
    for i, line in enumerate(m):
        if (i+1 >= len(m)):
            return
        diffs = 0
        diffs += checkDiffs(line, m[i+1])
        if diffs <= 1:
            stepper = 1
            foundReflection=True
            while i-stepper >= 0 and i + 1 + stepper < len(m):
                diffs += checkDiffs(m[i-stepper], m[i + 1 + stepper])
                if diffs > 1 :
                    foundReflection = False
                    break
                stepper+=1
            if foundReflection and diffs == 1:
                return i+1

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    maps = list()
    currentMap = list()
    for line in lines:
        if len(line) <= 1:
            maps.append(currentMap)
            currentMap = list()
        else:
            currentMap.append(line.strip())
    maps.append(currentMap)
        
    cumSum = 0
    for m in maps:
        vr = verticalReflection(m)
        if vr:
            cumSum += vr
            continue
        hr = horizontalReflection(m)
        if hr:
            cumSum += 100*hr

    return cumSum

if __name__ == '__main__':
    x = time.perf_counter_ns()
    answer = main()
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
