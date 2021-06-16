# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read

t,*data = map(int,read().split())
t = int(t)

def solve(m,pn0):
    pn = []
    tot = 0
    it = iter(pn0)
    for p,n in zip(it,it):
        pn.append([p,n])
        tot += p*n
    dp = [-1] * (tot+1)
    dp[1] = tot
    for p,n in pn:
        start = tot//p
        for j in range(start,0,-1):
            if dp[j] == -1:
                continue
            x = j
            for _ in range(n):
                x2 = x*p
                if x2 > tot:
                    break
                dp[x2] = dp[x] - p
                x = x2
    
    res = 0
    for i in range(tot,0,-1):
        if dp[i] == i:
            res = i
            break
    return res


ans = [''] * t
idx = 0
for i in range(t):
    m = data[idx]
    pn = data[idx+1:idx+1+m*2]
    idx += m*2+1
    res = solve(m,pn)
    ans[i] = 'Case #{}: {}'.format(i+1,res)
print('\n'.join(ans))

