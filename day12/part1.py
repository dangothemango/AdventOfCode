import time

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
        if segmentSize != int(segment):
            return 0
    return 1 if '#' not in values[vIndex:] else 0

def testQs(questionMarks, values, segments):
    index = questionMarks[0]
    cumSum = 0
    values[index] = '#'
    if (len(questionMarks) == 1):
        cumSum += verifyMap(values, segments)
        values[index]
    else:
        cumSum += testQs(questionMarks[1:], values, segments)
    values[index] = '.'
    if (len(questionMarks) == 1):
        cumSum += verifyMap(values, segments)
        values[index]
    else:
        cumSum += testQs(questionMarks[1:], values, segments)
    return cumSum

def main():
    with open('testInput.txt') as f:
        lines = f.readlines()

    cumSum = 0
    for line in lines:
        data = line.split(' ')
        values = list(data[0])
        segments = data[1].strip().split(',')
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
