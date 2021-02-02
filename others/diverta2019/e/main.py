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
mod = 10**9+7

tot_xor = 0
for ai in a:
    tot_xor ^= ai

a = [tot_xor] + a
cs_xor = [tot_xor]
cs_0 = [0]
for ai in a[1:]:
    cs_xor.append(cs_xor[-1] ^ ai)
    cs_0.append(cs_0[-1] + (cs_xor[-1]==0))

# print(cs_tot)
# print(cs_0)

dp = [[0,0] for _ in range(n+1)]
last = [-1] * (2**20)

for i,ci in enumerate(cs_xor):
    if(ci==0):
        continue
    if(last[ci] == -1):
        last[ci] = i
        if(tot_xor==0):
            dp[i] = [1,1]
        else:
            if(ci == tot_xor):
                dp[i] = [0,1]
    else:
        bef = last[ci]
        num_0 = cs_0[i] - cs_0[bef]
        dp[i][0] = (dp[bef][0] + dp[bef][1] * num_0)%mod
        dp[i][1] = (dp[i][0] + dp[bef][1])%mod
        last[ci] = i

ans = 0
for li in last:
    if(li==-1):
        continue
    ans += dp[li][1]
    ans %= mod

if(tot_xor == 0):
    num_0 = cs_0[-1] -1
    ans += pow(2,num_0,mod)
    ans %= mod
print(ans)




