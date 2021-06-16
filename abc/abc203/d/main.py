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

n,k,*data = map(int,read().split())
a = []
for i in range(n):
    a.append(data[i*n:i*n+n])

cent = (k**2 +1)//2 

def check(x):
    cs = [[0] * (n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            cs[i][j] = 1 * (a[i][j] <= x)
    
    for i in range(n):
        for j in range(1,n):
            cs[i][j] += cs[i][j-1]
    
    for i in range(1,n):
        for j in range(n):
            cs[i][j] += cs[i-1][j]
    # print(x,cs)
    
    for i in range(k-1,n):
        for j in range(k-1,n):
            cnt = cs[i][j] - cs[i-k][j] - cs[i][j-k] + cs[i-k][j-k]
            if cnt >= cent:
                return True
    return False

ng = -1
ok = 10**9
while ok - ng > 1:
    mid = (ok+ng)//2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)