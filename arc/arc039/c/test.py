# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

import random

def solve(k,s):
    # k = int(input())
    # s = input()

    # start を(200000,200000)としておく幅は400001
    point = dict()
    w = 400001
    x,y = 200000,200000
    point[x*w+y] = [200000,200000,200000,200000] #LRDU
    nums = {'L':0, 'R':1, 'D':2, 'U':3}

    for si in s:
        idx = nums[si]
        route = [[x,y]]
        while True:
            if idx < 2:
                x2 = point[x*w+y][idx]
                y2 = y
                if x == x2:
                    x2 += 1 if idx == 1 else -1
            else:
                x2 = x
                y2 = point[x*w+y][idx]
                if y == y2:
                    y2 += 1 if idx == 3 else -1
            x,y = x2,y2
            if not x*w+y in point:
                break
            route.append([x,y])
        
        if idx < 2:
            l = min(x,route[0][0])
            r = max(x,route[0][0])
            for a,b in route:
                ab = a*w+b
                point[ab][0] = l
                point[ab][1] = r
            xy = x*w+y
            point[xy] = [l,r,y,y]
        else:
            d = min(y,route[0][1])
            u = max(y,route[0][1])
            for a,b in route:
                ab = a*w+b
                point[ab][2] = d
                point[ab][3] = u
            xy = x*w+y
            point[xy] = [x,x,d,u]
    return [x-200000,y-200000]

    # print(x-200000,y-200000)

def solve_simple(k,s):
    done = set()
    x,y = 0,0
    done.add((x,y))
    for si in s:
        while (x,y) in done:
            if si == 'L':
                x -= 1
            elif si == 'R':
                x += 1
            elif si == 'D':
                y -= 1
            else:
                y += 1
        done.add((x,y))
    
    return [x,y]



for _ in range(100):
    k = random.randint(5,5000)
    s = ''
    for i in range(k):
        s += 'LRDU'[random.randint(0,3)]
    # print(k,s)
    res1 = solve(k,s)
    res2 = solve_simple(k,s)
    if res1 != res2:
        print(k,s)
        print(res1)
        print(res2)
        exit()