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

t,*case = map(int,read().split())
idx = 0
for _ in range(t):
    n = case[idx]
    p = case[idx+1:idx+1+n]
    idx += 1 + n

    if n == 2:
        if p == [1,2]:
            print(0)
            print()
        else:
            print(1)
            print(1)
        continue

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

    # return m,a
    print(m)
    print(' '.join(map(str,a)))
    # print(p)