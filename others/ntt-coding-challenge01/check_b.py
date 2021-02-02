# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
import glob

solve = 'B'

def sol(i):
    f_in = open(i,'r')
    sys.stdin = f_in

    n,m = map(int,input().split())
    x = [list(map(int,input().split())) for _ in range(n)]
    s = input()

    def calc(x,dir):
        if(dir in 'UD'):
            x = list(zip(*x))
        if(dir in 'DR'):
            x = list(map(lambda y: y[::-1] ,x))

        for i in range(len(x)):
            next = [0] * len(x[0])
            now = 0
            for j in x[i]:
                if(j==0):
                    continue
                if(next[now]==0):
                    next[now] = j
                    continue
                if(next[now] == j):
                    next[now] *= 2
                    now += 1
                else:
                    now += 1
                    next[now] = j
            x[i] = next[::]

        if(dir in 'DR'):
            x = list(map(lambda y: y[::-1] ,x))
        if(dir in 'UD'):
            x = list(zip(*x))

        return(x)

    for dir in s:
        x = calc(x,dir)

    # for i in x:
    #     print(' '.join(map(str,x)))
    return n,x


in_dir = './{}/input/*'.format(solve)
in_list = glob.glob(in_dir)

for i in in_list:
    print(i)
    j = i.replace('in','out')

    n,x = sol(i)
    f_out = open(j,'r')
    sys.stdin = f_out
    y = [list(map(int,input().split())) for _ in range(n)]

    # if(i == './B/input\\test3.in'):
    #     print(x)
    #     print(y)

    flag = False
    for i in range(n):
        for j in range(len(x[i])):
            if(x[i][j]!=y[i][j]):
                print('bad')
                flag = True
                break
        if(flag):
            break

    print('OK')







# f = open('../../input.txt', 'r')
# sys.stdin = f
