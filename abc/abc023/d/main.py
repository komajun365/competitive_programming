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

n,*data = map(int,read().split())

hs = []
it = iter(data)
for h,s in zip(it,it):
    hs.append([h,s])

def calc(x):
    times = []
    for h,s in hs:
        times.append((x-h) // s)
    
    times.sort()
    for i in range(n):
        if times[i] < i:
            return False
    return True

ng = 0
ok = 10**14 + 100
while ok-ng > 1:
    mid = (ok+ng)//2
    if calc(mid):
        ok = mid
    else:
        ng = mid
print(ok)