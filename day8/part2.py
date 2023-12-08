import time,math

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    directions = lines[0].strip().replace('L','0').replace('R','1')

    currentNodes = list()
    nodes = dict()
    for line in lines[2:]:
        data = line.split(' = ')
        if data[0].endswith('A'):
            currentNodes.append(data[0])
        nodes[data[0]] = data[1].strip('()\n').split(', ')

    print(currentNodes)
    # steps = 0
    # while len([x for x in currentNodes if not x.endswith('Z')]) > 0:
    #     direction = int(directions[steps%len(directions)])
    #     for i in range(len(currentNodes)):
    #         currentNodes[i] = nodes[currentNodes[i]][direction]
    #     steps += 1
    zSteps = []
    for node in currentNodes:
        n = node
        visited = dict()
        steps =0
        direction = int(directions[steps%len(directions)])
        while (n, direction, steps%len(directions)) not in visited:
            visited[(n,direction, steps%len(directions))] = steps
            n = nodes[n][direction]
            steps+=1
            direction = int(directions[steps%len(directions)])
        for b in [x for x in visited if x[0].endswith('Z')]:
            zSteps.append(visited[b])
            print(zSteps)
    lcm = 1
    for i in zSteps:
        lcm = lcm*i//math.gcd(lcm, i)
    return lcm

if __name__ == '__main__':
    x = time.perf_counter_ns()
    answer = main()
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
