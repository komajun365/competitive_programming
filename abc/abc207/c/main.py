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
tlr = []
it = iter(data)
for t,l,r in zip(it,it,it):
    l *= 2
    r *= 2
    if t == 2 or t == 4:
        r -= 1
    if t == 3 or t == 4:
        l += 1
    tlr.append([l,r])

ans = 0
for i in range(n-1):
    li,ri = tlr[i]
    for j in range(i+1,n):
        lj,rj = tlr[j]
        if lj <= li <= rj or lj <= ri <= rj or li <= lj <= ri or li <= rj <= ri:
            ans += 1
print(ans)
