import time

class Rule():

    def __init__(self, rString):
        self.noCondition = False
        if ':' not in rString:
            self.dest = rString
            self.noCondition = True
            return
        self.label = rString[0]
        if rString[1] == '<':
            self.func = self.lt
        else:
            self.func = self.gt
        colon = rString.index(':')
        self.value = int(rString[2:colon])
        self.dest = rString[colon+1:]

    def gt(self,a,b):
        return a>b
    
    def lt(self,a,b):
        return a<b
    
    def eval(self, part):
        if self.noCondition:
            return self.dest
        if (self.func(part[self.label],self.value)):
            return self.dest
        return None


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
    x,m,a,s='x','m','a','s'
    cumSum = 0
    while i < len(lines):
        part = eval(lines[i].replace('=', ':'))
        dest = 'in'
        while dest not in ['R', 'A']:
            rule = rules[dest]
            subRuleIndex = 0
            result = None
            while result == None:
                result = rule[subRuleIndex].eval(part)
                subRuleIndex += 1
            dest = result
        if dest == 'A':
            cumSum += sum(part.values())
        i+=1

    return cumSum

if __name__ == '__main__':
    x = time.perf_counter_ns()
    answer = main()
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
