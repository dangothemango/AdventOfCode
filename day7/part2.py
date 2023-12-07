import time

heirarchy = [
    'A','K','Q','T','9','8','7','6','5','4','3','2','J'
]

class Hand():

    def __init__(self, initString):
        data = initString.split(' ')
        self.cards = data[0]
        self.bid = int(data[1])
        counts = {}
        for n in self.cards:
            if n not in counts:
                counts[n] = 0
            counts[n] += 1
        if 'J' in counts and len(counts) > 1:
            maxCount=-1
            maxIndex=''
            for n in counts:
                if n == 'J':
                    continue
                if counts[n] > maxCount:
                    maxCount=counts[n]
                    maxIndex=n
            counts[maxIndex]= maxCount+counts['J']
            counts['J'] = 0
        self.value = 0
        for n in counts:
            self.value += 0 if counts[n] == 0 else counts[n]**counts[n]

    def __lt__(self, other):
        if self.value < other.value:
            return True
        elif other.value < self.value:
            return False
        for i in range(len(self.cards)):
            if heirarchy.index(self.cards[i]) > heirarchy.index(other.cards[i]):
                return True
            elif heirarchy.index(self.cards[i]) < heirarchy.index(other.cards[i]):
                return False
        return False

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    hands = list()
    for line in lines:
        hands.append(Hand(line.strip()))
    hands.sort()
    cumSum = 0
    for i, hand in enumerate(hands):
        cumSum += (i+1) * hand.bid
    return cumSum

if __name__ == '__main__':
    x = time.perf_counter_ns()
    answer = main()
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
