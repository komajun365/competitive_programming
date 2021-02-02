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
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from heapq import heappop,heappush

n,*data = map(int,read().split())

ab = []
it = iter(data)
for a,b in zip(it,it):
    ab.append([a,b])

ab.sort(key=lambda x: x[0]*-1)

hq = []
ans = [0]
for i in range(1,n+1):
    while(ab):
        if(ab[-1][0] <= i):
            a,b = ab.pop()
            heappush(hq,-1*b)
        else:
            break
    ans.append(ans[-1] - heappop(hq))

print('\n'.join(map(str,ans[1:])))
    

