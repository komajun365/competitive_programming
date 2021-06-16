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
it = iter(data)
ab = [[a,b] for a,b in zip(it,it)]
ab.sort()
now = k
idx = 0
while idx < n:
    if ab[idx][0] <= now:
        now += ab[idx][1]
        idx += 1
    else:
        break
print(now)