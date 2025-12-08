#!/usr/bin/env python3
import time, re
from aocd import data, submit
from math import sqrt

EXAMPLE_DATA='''162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689'''
EXAMPLE_ANSWER=40

def dist(a, b):
    a = a.split(',')
    b = b.split(',')
    a[0],a[1],a[2]=int(a[0]),int(a[1]),int(a[2])
    b[0],b[1],b[2]=int(b[0]),int(b[1]),int(b[2])
    d = sqrt(((a[0]-b[0])**2)+((a[1]-b[1])**2)+((a[2]-b[2])**2))
    return d

def main(data, num):
    distances = dict()
    data = data.splitlines()
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            distances[(i,j)] = dist(data[i], data[j])
    sorted_items_asc = sorted(distances.items(), key=lambda item: item[1])
    sortedDistances = list(dict(sorted_items_asc).keys())
    groups=list()
    i=0
    while i < num:
        x = sortedDistances.pop(0)
        foundGroups = list()
        for j, group in enumerate(groups):
            if x[0] in group or x[1] in group:
                foundGroups.append(j)
                group.add(x[0])
                group.add(x[1])

        if len(foundGroups) == 0:
            groups.append(set([x[0],x[1]]))
        elif len(foundGroups) > 1:
            g = groups[foundGroups[0]]
            for j in foundGroups[:0:-1]:
                g.update(groups[j])
                groups.pop(j)
        i+=1
    groups.sort(key=len, reverse=True)
    return len(groups[0]) * len(groups[1]) * len(groups[2])
    

if __name__ == '__main__':
    ex_answer=main(EXAMPLE_DATA, 10)
    print('Example Answer:', ex_answer)
    assert ex_answer == EXAMPLE_ANSWER
    x = time.perf_counter_ns()
    answer = main(data, 1000)
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
    submit(answer)
