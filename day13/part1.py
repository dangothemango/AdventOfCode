import time

def verticalReflection(m):
    return horizontalReflection(list(zip(*m)))

def horizontalReflection(m):
    for i, line in enumerate(m):
        if i+1 < len(m) and line == m[i+1]:
            #print(line,'=',m[i+1])
            stepper = 1
            foundReflection=True
            while i-stepper >= 0 and i + 1 + stepper < len(m):
                #print('fr', i)
                if m[i-stepper] != m[i + 1 + stepper]:
                    foundReflection = False
                    break
                stepper+=1
            if foundReflection:
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
        for l in m:
            print (''.join(l))
        print('vertical')
        vr = verticalReflection(m)
        print(vr)
        if vr:
            cumSum += vr
            continue
        print('horizontal')
        hr = horizontalReflection(m)
        print(hr)
        if hr:
            cumSum += 100*hr

    return cumSum

if __name__ == '__main__':
    x = time.perf_counter_ns()
    answer = main()
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
