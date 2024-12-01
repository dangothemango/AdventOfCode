import re

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    numbers = set()
    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(line)):
            if not line[x].isdigit() and not line[x] == '.':
                for i in range(-1,2):
                    for j in range(-1,2):
                        xIndex = x+i
                        yIndex = y+j
                        if xIndex < 0 or yIndex<0 or yIndex >= len(lines) or xIndex>= len(line):
                            continue
                        if (lines[yIndex][xIndex].isdigit()):
                            number=lines[yIndex][xIndex]
                            searchX = xIndex - 1
                            while searchX >=0 and lines[yIndex][searchX].isdigit():
                                number = lines[yIndex][searchX] + number
                                searchX -= 1
                            startX = searchX + 1
                            searchX = xIndex + 1
                            while searchX < len(line) and lines[yIndex][searchX].isdigit():
                                number = number + lines[yIndex][searchX] 
                                searchX += 1
                            numbers.add((startX, yIndex, int(number)))
                            print((startX, yIndex,  int(number)))
    sum = 0
    for n in numbers:
        sum += n[2]
    print(sum)




if __name__ == '__main__':
    main()
