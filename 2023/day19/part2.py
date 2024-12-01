import time

class Rule():

    def __init__(self, rString):
        self.noCondition = False
        if ':' not in rString:
            self.dest = rString
            self.noCondition = True
            return
        self.label = rString[0]
        self.func = rString[1]
        # if rString[1] == '<':
        #     self.func = self.lt
        # else:
        #     self.func = self.gt
        colon = rString.index(':')
        self.value = int(rString[2:colon])
        self.dest = rString[colon+1:]

    def gt(self,a,b):
        return a>b
    
    def lt(self,a,b):
        return a<b
    
    def bisectRange(self, part):
        if self.noCondition:
            return part, self.dest, None
        partRange = part[self.label]
        if self.func == '<':
            if partRange[1] < self.value:
                return part,self.dest,None
            if partRange[0] >= self.value:
                return None,None,part
            aPart = dict(part)
            rPart = dict(part)
            aPart[self.label] = [partRange[0], self.value-1]
            rPart[self.label] = [self.value, partRange[1]]
            return aPart, self.dest, rPart
        else:
            if partRange[0] > self.value:
                return part,self.dest,None
            if partRange[1] <= self.value:
                return None,None,part
            aPart = dict(part)
            rPart = dict(part)
            aPart[self.label] = [self.value+1, partRange[1]]
            rPart[self.label] = [partRange[0], self.value]
            return aPart, self.dest, rPart
        


def main():
    with open('input.txt') as f:
        lines = f.readlines()

    rules = dict()
    i = 0
    while len(lines[i])>1:
        data = lines[i].strip('\n}').split('{')
        d = list()
        for rule in data[1].split(','):
            d.append(Rule(rule))
        rules[data[0]] = d
        i+=1

    i+=1
    acceptedRanges = []
    ranges = [{
        'x':[1,4000],
        'm':[1,4000],
        'a':[1,4000],
        's':[1,4000],
        'd':'in'
    }]
    while len(ranges) > 0:
        range = ranges.pop()
        rule = rules[range['d']]
        for subRule in rule:
            # print(range)
            aPart, aDest, rPart = subRule.bisectRange(range)
            # print(aPart, aDest, rPart)
            if aPart:
                if aDest == 'A':
                    del aPart['d']
                    acceptedRanges.append(aPart)
                elif aDest != 'R':
                    aPart['d'] = aDest
                    ranges.append(aPart)
            range = rPart
            if not range:
                break

    cumSum = 0
    for r in acceptedRanges:
        cumProduct = 1
        for v in r.values():
            cumProduct *= v[1]-v[0]+1
        cumSum+=cumProduct

    return cumSum

if __name__ == '__main__':
    x = time.perf_counter_ns()
    answer = main()
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
