import time,re

def main():
    with open('input.txt') as f:
        lines = f.readlines()
    
    data = lines[0].strip().split(',')

    cumSum = 0
    for word in data:
        curVal = 0
        for char in word:
            curVal = ((curVal + ord(char)) * 17) % 256
        cumSum+=curVal

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
