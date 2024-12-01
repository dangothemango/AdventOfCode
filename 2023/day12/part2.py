import time
cache = dict()

def verifyMap(values, segments):
    vIndex = 0
    segments = list(segments)
    while len(segments) > 0:
        segment = segments.pop(0)
        while vIndex < len(values) and values[vIndex] == '.':
            vIndex += 1
        segmentSize = 0
        while vIndex < len(values) and values[vIndex] == '#':
            segmentSize += 1
            vIndex += 1
            if (segmentSize > segment):
                return vIndex*-1
        if segmentSize != segment:
            return vIndex*-1
    return 1 if '#' not in values[vIndex:] else (-1 * (values[vIndex:].index('#')+vIndex) - 1)

def testQs(questionMarks, values, segments):
    index = questionMarks[0]
    cumSum = 0
    i = 0
    segments2 = list()
    while i < index:
        while i < index and values[i] == '.':
            i+=1
        segmentSize = 0
        while i < index and values[i] == '#':
            segmentSize += 1
            i+=1
        segments2.append(segmentSize)
    if (values[index-1], index, str(segments2)) in cache:
        return cache[(values[index-1], index, str(segments2))]
    if values[:index].count('#') < sum(segments):
        values[index] = '#'

        if (len(questionMarks) == 1):
            result = verifyMap(values, segments)
            if result < 0:
                if (result + index > 0):
                    return result
            else:
                cumSum += result
                
        else:
            result = testQs(questionMarks[1:], values, segments)
            if result < 0:
                if (result + index > 0):
                    return result
            else:
                cumSum += result
    values[index] = '.'
    if (len(questionMarks) == 1):
        result = verifyMap(values, segments)
        if result < 0:
            if (result + index > 0):
                return result
        else:
            cumSum += result
    else:
        result = testQs(questionMarks[1:], values, segments)
        if result < 0:
            if (result + index > 0):
                return result
        else:
            cumSum += result
    cache[(values[index-1], index, str(segments2))]=cumSum
    return cumSum

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    cumSum = 0
    for line in lines:
        cache.clear()
        data = line.split(' ')
        values = (list(data[0]+'?')*5)[:-1]
        segments = [int(x) for x in data[1].strip().split(',')*5]
        questionMarks = list()
        for i, char in enumerate(values):
            if char == '?':
                questionMarks.append(i)
        checkNumbers = testQs(questionMarks,values,segments)
        print(checkNumbers, ''.join(values))
        cumSum += checkNumbers

    return cumSum

if __name__ == '__main__':
    x = time.perf_counter_ns()
    answer = main()
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
