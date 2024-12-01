
import sys, time

def fillInMapGaps(map):
    l = 0
    newMaps = list()
    for mapping in map:
        u = mapping.lowerBound
        if l != u:
            newMaps.append(Mapping('{} {} {}'.format(l,l,u-l)))
        l = mapping.upperBound
    newMaps.append(Mapping('{} {} {}'.format(l,l,sys.maxsize)))
    for m in newMaps:
        map.append(m)
    map.sort()

class Mapping():

    def __init__(self, inputString):
        values = inputString.split(' ')
        self.lowerBound = int(values[1])
        self.upperBound = self.lowerBound + int(values[2])
        self.difference = self.lowerBound - int(values[0])

    def __lt__(self, other):
        return self.lowerBound < other.lowerBound

    def convertNumber(self, num):
        if num >= self.lowerBound and num < self.upperBound:
            cNum = num - self.difference
            return cNum, self.upperBound - num
        return None, None

class Range():

    def __init__(self,tup):
        self.lowerBound = tup[0]
        self.size = tup[1]

    def __lt__(self, other):
        return self.lowerBound < other.lowerBound

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    seeds = lines[0].strip().split(': ')[1].split(' ')
    seedRanges = list()

    for i in range(0,len(seeds),2):
        seedRanges.append(Range((int(seeds[i]),int(seeds[i+1]))))
    
    seedRanges.sort()

    maps=list()

    lines = ''.join(lines[1:])
    for map in lines[1:].split(':\n')[1:]:
        strings = map.split('\n')[:-1]
        mappings = list()
        for string in strings:
            if len(string) > 0:
                mappings.append(Mapping(string))
        mappings.sort()
        maps.append(mappings)

    sourceRanges = seedRanges
    subRange = None
    for map in maps:
        fillInMapGaps(map)
        destRanges = list()
        for sourceRange in sourceRanges:
            startNum = sourceRange.lowerBound
            size = sourceRange.size
            while size > 0:
                result = None
                i = 0
                while result == None and i < len(map):
                    result, remaining = map[i].convertNumber(startNum)
                    i+=1
                destRanges.append(Range((result, min(remaining,size))))
                size -= remaining
                startNum += remaining
        sourceRanges = destRanges

    sourceRanges.sort()
    print(sourceRanges[0].lowerBound)
            
    

if __name__ == '__main__':
    x = time.perf_counter_ns()
    main()
    y = time.perf_counter_ns()
    print(y-x)
