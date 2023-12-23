import time

class Module():

    def __init__(self, label, dests):
        self.dests = list(dests)
        self.label = label
        self.inputs = dict()

    def addDests(self, dests):
        self.dests.extend(dests)

    def pulse(self, pulse, input):
        return None
    
    def addInput(self, input):
        pass
    
    def __str__(self):
        return '{} {}: {} -> {}'.format(type(self), self.label, self.inputs, self.dests)

class Broadcaster(Module):
    def pulse(self, pulse, input):
        return pulse

class FlipFlop(Module):

    def __init__(self, label, dests):
        Module.__init__(self, label, dests)
        self.state = False

    def pulse(self, pulse, input):
        if pulse == True:
            return None
        self.state = not self.state
        return self.state
        
class Conjuction(Module):

    def pulse(self, pulse, input):
        self.inputs[input] = pulse
        return False in self.inputs.values()
    
    def addInput(self, label):
        self.inputs[label] = False

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    modules = dict()
    lostInputs = list()
    for line in lines:
        data = line.strip().split(' -> ')
        label = data[0][1:]
        print(label)
        mType = data[0][0]
        dests = data[1].split(', ')
        if mType == '%':
            modules[label] = FlipFlop(label, dests)
        elif mType == '&':
            modules[label] = Conjuction(label, dests)
        elif mType == '+':
            modules[label] = Broadcaster(label, dests)
        for d in dests:
            if d in modules:
                modules[d].addInput(label)
            else:
                lostInputs.append((label,d))
    for li in lostInputs:
        if (li[1]) not in modules:
            modules[li[1]] = Module(li[1], [])
        modules[li[1]].addInput(li[0])
    
    for module in modules.values():
        print(module)

    lowPulses = 0
    highPulses = 0
    x=0
    while True:
        x+=1
        pulses = list()
        pulses.append(('broadcaster', False, 'button'))
        while len(pulses) > 0:
            label, power, source = pulses.pop(0)
            if label == 'rx' and not power:
                return x
            if power:
                highPulses+=1
            else:
                lowPulses+=1
            module = modules[label]
            result = module.pulse(power,source)
            if result != None:
                for d in module.dests:
                    pulses.append((d, result, label))
    print(lowPulses, highPulses)

    return lowPulses * highPulses

if __name__ == '__main__':
    x = time.perf_counter_ns()
    answer = main()
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
