
import re

def main():
    with open('input.txt') as f:
        lines = f.readlines()
    
    sum = 0
    for line in lines:
        numbers = re.sub(r'[a-zA-Z]+','',line.strip())
        print(numbers)
        num = numbers[0] + numbers[-1]
        sum += int(num)
    print(sum)

if __name__ == '__main__':
    main()
