import sys

class Mapping():

    def __init__(self, inputString):
        values = inputString.split(' ')
        self.lowerBound = int(values[1])
        self.upperBound = self.lowerBound + int(values[2])
        self.difference = self.lowerBound - int(values[0])

    def __str__(self):
        return str((self.lowerBound, self.upperBound, self.difference))

    def __lt__(self, other):
        return self.lowerBound < other.lowerBound

    def __gt__(self, other):
        return self.lowerBound > other.lowerBound

    def convertNumber(self, num):
        if num >= self.lowerBound and num < self.upperBound:
            return num - self.difference
        return None

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    seeds = lines[0].strip().split(': ')[1].split(' ')

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
    
    minLoc = sys.maxsize
    for seed in seeds:
        seed = int(seed)
        source = seed
        for map in maps:
            result = None
            i = 0
            while result == None and i < len(map):
                result = map[i].convertNumber(source)
                i+=1
            if result:
                source = result
        minLoc = min(minLoc, source)
    
    print(minLoc)
        

if __name__ == '__main__':
    main()
