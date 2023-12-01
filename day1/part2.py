
import re

numStrings = ['','one','two','three','four','five','six','seven','eight','nine']

def findNumbers(line):
    numbers = []
    for j in range(len(line)):
        if re.search(r'\d',line[j]):
            numbers.append(line[j])
            continue
        for i in range(1, len(numStrings)):
            if line[j:j+len(numStrings[i])] == numStrings[i]:
                numbers.append(str(i))
    return numbers

        

def main():
    with open('input.txt') as f:
        lines = f.readlines()
    
    sum = 0
    for line in lines:
        numbers = findNumbers(line.strip())
        print(line)
        num = numbers[0] + numbers[-1]
        sum += int(num)
    print(sum)

if __name__ == '__main__':
    main()
