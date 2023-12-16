import time,re

def main():
    with open('input.txt') as f:
        lines = f.readlines()
    
    data = lines[0].strip().split(',')

    boxes = dict()
    cumSum = 0
    for word in data:
        curVal = 0
        splitWord = re.split(r'-|=',word)
        for char in splitWord[0]:
            curVal = ((curVal + ord(char)) * 17) % 256
        if curVal not in boxes:
            boxes[curVal] = []
        if len(splitWord[1]) == 0:
            for lens in boxes[curVal]:
                if lens[0] == splitWord[0]:
                    boxes[curVal].remove(lens)
                    break
        else:
            inserted = False
            for i, lens in enumerate(boxes[curVal]):
                if lens[0] == splitWord[0]:
                    boxes[curVal][i] = (splitWord[0],int(splitWord[1]))
                    inserted = True
                    break
            if not inserted:
                boxes[curVal].append((splitWord[0],int(splitWord[1])))

    for boxNumber in boxes:
        for i, lens in enumerate(boxes[boxNumber]):
            cumSum += (boxNumber + 1)*(i+1)*(lens[1])

    return cumSum

if __name__ == '__main__':
    x = time.perf_counter_ns()
    answer = main()
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)

# Determine the ASCII code for the current character of the string.
# Increase the current value by the ASCII code you just determined.
# Set the current value to itself multiplied by 17.
# Set the current value to the remainder of dividing itself by 256.
