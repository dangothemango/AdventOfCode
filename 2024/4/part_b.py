import time, re
from aocd import data, submit

EXAMPLE_DATA='''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''
EXAMPLE_ANSWER=9

directions=[(1,1), (-1,-1),(1,-1),(-1,1),(1,0),(-1,0),(0,1),(0,-1)]

def getAtCoord(lines, coord):
    if coord[0] >= len(lines) or coord[0] < 0 or coord[1] >= len(lines[coord[0]]) or coord[1] < 0:
        #return '~' should trigger the same failures when looking for x-mas
        return '~'
    return lines[coord[0]][coord[1]]

def main(data):
    lines=data.split('\n')
    found_count=0
    for r_index, row in enumerate(lines):
        for c_index, letter in enumerate(row):
            if letter == 'A':
                a=getAtCoord(lines,(r_index-1,c_index-1)) + getAtCoord(lines,(r_index+1,c_index+1))
                b=getAtCoord(lines,(r_index+1,c_index-1)) + getAtCoord(lines,(r_index-1,c_index+1))
                print(a,b)
                if (a=='MS' or a=='SM') and (b=='MS' or b=='SM'):
                    found_count+=1
    print(found_count)
    return found_count

def check_direction(lines, prev, dir, S_INDEX):
    if S_INDEX==len(SEARCH):
        return True
    new=(prev[0]+dir[0], prev[1]+dir[1])
    if new[0] >= len(lines) or new[0] < 0 or new[1] >= len(lines[new[0]]) or new[1] < 0 or lines[new[0]][new[1]] != SEARCH[S_INDEX]:
        return False
    return check_direction(lines, new, dir, S_INDEX+1)

if __name__ == '__main__':
    assert main(EXAMPLE_DATA) == EXAMPLE_ANSWER
    print(data)
    x = time.perf_counter_ns()
    answer = main(data)
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000000)
    submit(answer)
