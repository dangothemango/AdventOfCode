import time,re, math

def main():
    with open('input.txt') as f:
        lines = f.readlines()


    times = re.findall(r'\d+', lines[0])
    distances = re.findall(r'\d+', lines[1])
    times = [''.join(times)]
    distances = [''.join(distances)]
    possibleWins = list()
    for i in range(len(times)):
        time = int(times[i])
        distance = int(distances[i])
        guess = math.ceil(distance/time)
        print(guess)
        while guess * (time-guess) <= distance:
            guess = math.ceil(distance/(time-guess))
            print(guess)
        possibleWins.append(time-2*guess+1)
        print('------')
            
    return math.prod(possibleWins)

if __name__ == '__main__':
    x = time.perf_counter_ns()
    answer = main()
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
