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

n,m,*xyz = map(int,read().split())

yz = [[] for _ in range(n)]
it = iter(xyz)
for x,y,z in zip(it,it,it):
    x -= 1
    y -= 1
    yz[x].append([y,z])

def calc(bit):
    cnt = [0] * n
    for i in range(n):
        cnt[i] += cnt[i-1]
        if (bit >> i) & 1:
            cnt[i] += 1

    flags = cnt[-1]
    for y,z in yz[flags-1]:
        if cnt[y] > z:
            return 0
    
    res = 0
    for i in range(n):
        if (bit >> i) & 1:
            res += dp[bit ^ (1<<i)]
    return res
    
dp = [0] * (1<<n)
dp[0] = 1
for bit in range(1,1<<n):
    dp[bit] = calc(bit)

print(dp[-1])
    
    






