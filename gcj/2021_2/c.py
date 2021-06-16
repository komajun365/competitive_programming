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

# tmp = 0
# for i in range(3,10**6+1):
#     tmp += 10**6//i
# print(tmp)

import sys
read = sys.stdin.buffer.read

t,*data = map(int,read().split())
mod = 10**9 + 7

## nCkのmodを求める関数
# テーブルを作る(前処理)
max_n = 10**5 + 10
fac, finv, inv = [0]*max_n, [0]*max_n, [0]*max_n

def comInit(max_n):
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1

    for i in range(2,max_n):
      fac[i] = fac[i-1]* i% mod
      inv[i] = mod - inv[mod%i] * (mod // i) % mod
      finv[i] = finv[i-1] * inv[i] % mod

comInit(max_n)

# 二項係数の計算
def com(n,k):
    if(n < k):
        return 0
    if( (n<0) | (k < 0)):
        return 0
    return fac[n] * (finv[k] * finv[n-k] % mod) % mod

def solve(n,v):
    for i in range(n-1):
        if v[i] > i+1 or v[i] + 1 < v[i+1]:
            return 0
    
    links = [[] for _ in range(n)]
    deg_in = [0] * n
    stack = []
    for i,vi in enumerate(v):
        if len(stack) >= vi:
            for j in range(vi-1 ,len(stack)-1):
                a,b = stack[j:j+2]
                links[b].append(a)
                deg_in[a] += 1
            for _ in range(len(stack) - vi):
                stack.pop()
            links[stack[-1]].append(i)
            deg_in[i] += 1
            stack.pop()
        stack.append(i)
        # print(n,stack)
        # print(links)
    for i in range(len(stack)-1):
        links[stack[i+1]].append(stack[i])
        deg_in[stack[i]] += 1
    # print(links)

    nums = [[] for _ in range(n)]
    dp = [1] * n
    stack = []
    for i in range(n):
        if deg_in[i] == 0:
            stack.append(i)
    
    res = 1
    while stack:
        i = stack.pop()
        tot = sum(nums[i])
        for num in nums[i]:
            dp[i] *= com(tot,num)
            dp[i] %= mod
            tot -= num
        for p in links[i]:
            nums[p].append(sum(nums[i])+1)
            dp[p] *= dp[i]
            dp[p] %= mod
            deg_in[p] -= 1
            if deg_in[p] == 0:
                stack.append(p)
    # print(dp)
    # print(nums)
    # print(i)
    # print(deg_in)

    return dp[i]

ans = [''] * t
idx = 0
for i in range(t):
    n = data[idx]
    v = data[idx+1:idx+1+n]
    idx += n+1
    res = solve(n,v)
    ans[i] = 'Case #{}: {}'.format(i+1,res)
print('\n'.join(ans))

