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

import sys
read = sys.stdin.buffer.read
from random import randint,shuffle

# t,*case = map(int,read().split())
# idx = 0
# for _ in range(t):
    # n = case[idx]
    # p = case[idx+1:idx+1+n]
    # idx += 1 + n

def solve(n,p):
    if n == 2:
        if p == [1,2]:
            m = 0
            a = []
            # print(0)
            # print()
        else:
            m = 1
            a = [1]
            # print(1)
            # print(1)
        # continue
        return m,a

    a = []
    m = 0
    def move(x,m):
        a.append(x+1)
        p[x],p[x+1] = p[x+1],p[x]
        return m+1
    
    if n % 2 == 0:
        m0 = n-2
        m1 = n-3
    else:
        m0 = n-3
        m1 = n-2
    
    for i in range(1,n-2):
        for j in range(i-1,n):
            if p[j] == i:
                break
        if j == i-1:
            continue
        if m % 2 == j % 2:
            if j == n-2:
                m = move(n-2,m)
                m = move(n-3,m)
                j = n-1
            elif j == n-3:
                m = move(n-3,m)
                m = move(n-2,m)
                m = move(n-3,m)
                j = n-1
            elif m % 2 == 0:
                m = move(m0,m)
            else:
                m = move(m1,m)

        for x in range(j-1,i-2,-1):
            m = move(x,m)
    
    while p[n-3:] != [n-2,n-1,n]:
        if m % 2 == 0:
            m = move(m0,m)
        else:
            m = move(m1,m)

    return m,a
    # print(m)
    # print(' '.join(map(str,a)))
    # print(p)

for _ in range(100):
    n = randint(2,200)
    p = list(range(1,n+1))
    shuffle(p)
    p2 = p[::]
    # print(n,p)

    m,a = solve(n,p2)
    if m > n**2:
        print(n,p)
        print(m)
        print(a)
        exit()
    if m != len(a):
        print(n,p)
        print(m)
        print(a)
        exit()
    
    x = p[::]
    for i in range(m):
        ai = a[i]-1
        if ai % 2 != i % 2:
            print(n,p)
            print(m)
            print(a)
            exit()
        x[ai],x[ai+1] = x[ai+1],x[ai]
    
    if x != list(range(1,n+1)):
        print(n,p)
        print(m)
        print(a)
        print(x)
        exit()



