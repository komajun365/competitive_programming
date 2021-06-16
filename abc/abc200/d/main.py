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

n = int(input())
a = list(map(int,input().split()))

rem = [-1] * 200
l = min(8,n)
for i in range(1,2**l):
    tmp = 0
    for j in range(l):
        if (i >> j) & 1:
            tmp += a[j]
    tmp %= 200
    if rem[tmp] != -1:
        b = []
        c = []
        for j in range(l):
            if (rem[tmp] >> j) & 1:
                b.append(j+1)
            if (i >> j) & 1:
                c.append(j+1)
        b = [len(b)] + b
        c = [len(c)] + c
        print('Yes')
        print(*b, sep=' ')
        print(*c, sep=' ')
        exit()
    rem[tmp] = i

print('No')

