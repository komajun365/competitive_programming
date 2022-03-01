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
from heapq import heappop,heappush

t,*data = map(int,read().split())

def solve(n,lr):
    lr2 = []
    it = iter(lr)
    for l,r in zip(it,it):
        lr2.append([l,r])
    lr2.sort()

    hq = []
    last = 0
    idx = 0
    # print(lr2)
    while idx < n or hq:
        # print(idx,last,hq)
        if len(hq) == 0:
            last = lr2[idx][0]
        
        while idx < n:
            if lr2[idx][0] == last:
                heappush(hq, lr2[idx][1])
            else:
                break
            idx += 1
        
        cand = heappop(hq)
        if cand < last:
            return 'No'
        last += 1
    return 'Yes'

ans = []
idx = 0
for _ in range(t):
    n = data[idx]
    lr = data[idx+1:idx+1+2*n]
    ans.append(solve(n,lr))
    idx += 1 + 2*n
print('\n'.join(ans))


