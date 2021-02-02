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
f = open('../../input.txt', 'r')
sys.stdin = f

from collections import deque

# n = int(input())
# a = list(map(int,input().split()))

import random
n = 7
a = [random.randint(1, 100) for i in range(n)]


def calc(n,a):

    p = [0] * (n-1)
    m = [0] * (n-1)

    for i in range(n-1):
        x,y = a[i:i+2]
        cnt = 0
        if(x > y):
            while(x>y):
                y *= 4
                cnt += 2
        else:
            x *= 4
            while(x<=y):
                x*=4
                cnt -= 2
        p[i] = cnt

    for i in range(n-1):
        x,y = a[i:i+2]
        cnt = 0
        if(x < y):
            while(x<y):
                x *= 4
                cnt += 2
        else:
            y *= 4
            while(x>=y):
                y*=4
                cnt -= 2
        m[i] = cnt

    cumsum_p = [0] * (n+1)
    cumsum_m = [0] * (n+1)

    d = deque()
    for i in range(n-2,-1,-1):
        cumsum_p[i] = cumsum_p[i+1]
        if(p[i] < 0):
            d.appendleft((i,p[i]))
        elif(p[i] > 0):
            cnt = p[i]
            while(d):
                j,rem_j = d.popleft()
                if(cnt + rem_j <= 0):
                    cumsum_p[i] += (j-i) * cnt
                    if(cnt + rem_j < 0):
                        d.appendleft((j,cnt + rem_j))
                    cnt = 0
                    break
                else:
                    cumsum_p[i] += (j-i) * (-1 * rem_j)
                    cnt = cnt + rem_j
            cumsum_p[i] += (n-i-1) * cnt

    d = deque()
    cumsum_m[1] = 1
    for i in range(n-1):
        cumsum_m[i+2] = cumsum_m[i+1] + 1
        if(m[i] < 0):
            d.appendleft((i,m[i]))
        elif(m[i] > 0):
            cnt = m[i]
            while(d):
                j,rem_j = d.popleft()
                if( cnt + rem_j <= 0 ):
                    cumsum_m[i+2] += (i-j) * cnt
                    if( cnt + rem_j < 0):
                        d.appendleft((j,cnt + rem_j))
                    cnt = 0
                    break
                else:
                    cumsum_m[i+2] += (i-j) * (-1*rem_j)
                    cnt = cnt + rem_j
            cumsum_m[i+2] += (i+1) * cnt

    ans = cumsum_p[0]
    for i in range(n+1):
        ans = min(ans, cumsum_p[i] + cumsum_m[i])

    return(ans)

def calc_simple(n,a):
    inf = 10**10
    ans = inf

    for i in range(n+1):
        pa = a[i:]
        ma = a[:i]
        tmp = 0
        if(len(pa) > 1):
            for j in range(len(pa)-1):
                while(pa[j] > pa[j+1]):
                    tmp += 2
                    pa[j+1] *= 4
        for j in range(len(ma)):
            tmp += 1
            ma[j] *= -2
        if(len(ma) > 1):
            for j in range(len(ma)-1,0,-1):
                while(ma[j-1] > ma[j]):
                    tmp += 2
                    ma[j-1] *= 4
        ans = min(ans,tmp)

    return ans

for _ in range(10000):
    n = 20
    a = [random.randint(1, 1000) for i in range(n)]
    ans1 = calc(n,a)
    ans2 = calc_simple(n,a)
    if(ans1 != ans2):
        print(ans1,ans2)
        print(n)
        print(a)
        exit()
