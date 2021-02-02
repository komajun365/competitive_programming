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

solve = 'C'

def sol(i):
    f_in = open(i,'r')
    sys.stdin = f_in
    import bisect
    from collections import defaultdict

    n,m = map(int,input().split())
    l = list(map(int,input().split()))

    l.sort()
    l_2 = [i**2 for i in l]

    ans_0 = 0
    d = defaultdict(int)
    for i in range(n-1):
        for j in range(i+1,n):
            other = l_2[j] + l_2[i]
            num = bisect.bisect_right(l_2,other) - bisect.bisect_left(l_2,other)
            ans_0 += num
            d[other] += 1
            dif = l_2[j] - l_2[i]
            if(dif>0):
                d[dif] += 1

    for i in range(n):
        d[l_2[i]/2] *= 1

    ans = 0
    for key,val in d.items():
        # m1
        m1 = val * m
        # m2
        m2 = bisect.bisect_right(l_2,key*2) - bisect.bisect_left(l_2,key*2)
        m2 *= (m * (m-1))//2
        ans = max(ans, m1+m2)

    # print(l_2)
    # print(d)

    return ans + ans_0





in_dir = './{}/input/*'.format(solve)
in_list = glob.glob(in_dir)

for i in in_list:
    # if(i != './C/input\\00-sample1.in'):
    #     continue
    print(i)
    j = i.replace('in','out')

    x = sol(i)
    f_out = open(j,'r')
    sys.stdin = f_out
    y = int(input())

    # print(x,y)

    if(x == y):
        print('OK')
    else:
        print('NG')

    # if(i == './B/input\\test3.in'):
    #     print(x)
    #     print(y)

    # flag = False
    # for i in range(n):
    #     for j in range(len(x[i])):
    #         if(x[i][j]!=y[i][j]):
    #             print('bad')
    #             flag = True
    #             break
    #     if(flag):
    #         break
    #
    # print('OK')







# f = open('../../input.txt', 'r')
# sys.stdin = f
