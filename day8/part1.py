import time

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    directions = lines[0].strip().replace('L','0').replace('R','1')

    nodes = {}
    for line in lines[2:]:
        data = line.split(' = ')
        nodes[data[0]] = data[1].strip('()\n').split(', ')

    steps = 0
    node = 'AAA'
    while node != 'ZZZ':
        direction = int(directions[steps%len(directions)])
        node = nodes[node][direction]
        steps += 1

    return steps

if __name__ == '__main__':
    x = time.perf_counter_ns()
    answer = main()
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000)
