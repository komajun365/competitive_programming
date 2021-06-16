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

def calc(x):
    res = 0
    up = []
    for i in range(n-1):
        if x[i] <= x[i+1]:
            up.append(x[i:i+2])
    up.sort()

    max_d = 0
    for i,j in up:
        tmp = 2 * (min(j,max_d) - i)
        res = max(tmp,res)
        max_d = max(max_d,j)
    
    return res

dif = max(0, calc(a), calc(a[::-1]))
for i in range(n-1):
    tmp = abs(a[i] - a[i+1]) - abs(a[i] - a[-1])
    dif = max(dif,tmp)
for i in range(1,n):
    tmp = abs(a[i] - a[i-1]) - abs(a[i] - a[0])
    dif = max(dif,tmp)

ans = -1 * dif
for i in range(n-1):
    ans += abs(a[i] - a[i+1])
print(ans)



