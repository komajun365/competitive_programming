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

x = list(range(2**n))
while(len(x) > 2):
    y = []
    l = len(x)
    for i in range(l//2):
        j = x[i*2]
        k = x[i*2+1]
        if a[j] > a[k]:
            y.append(j)
        else:
            y.append(k)
    if l % 2 == 1:
        y.append(x[-1])
    x,y = y,x

j,k = x
if a[j] > a[k]:
    print(k+1)
else:
    print(j+1)
