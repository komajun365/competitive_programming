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

s = input()
k = int(input())
mod = 10**9 + 7
l = len(s)
q = s.count('?')

if q == 0:
    cnt = 0
    for i in range(l-1):
        if s[i] != s[i+1]:
            cnt += 1
    cnt *= k
    if s[0] != s[-1]:
        cnt += k-1
    cnt = (cnt+1)//2
    cnt %= mod
    print(cnt)
    exit()



def calc(cnt):
    dp = [[0,0] for _ in range(l+1)]
    for i in range(l):
        if s[i] == '0':
            dp[i+1][0] = (dp[i][0] + dp[i][1] + cnt[1]) % mod
            cnt[0] = sum(cnt)
            cnt[0] %= mod
            cnt[1] = 0
            cnt[2] = 0
        elif s[0] == '1':
            dp[i+1][1] = (dp[i][0] + dp[i][1] + cnt[0]) % mod
            cnt[1] += sum(cnt)
            cnt[1] %= mod
            cnt[0] = 0
            cnt[2] = 0
        else:
            dp[i+1][0] = (dp[i][0] + dp[i][1] + cnt[1]) % mod
            dp[i+1][1] = (dp[i][0] + dp[i][1] + cnt[0]) % mod
            cnt[0] = sum(cnt) % mod
            cnt[1] = cnt[0]
            cnt[2] = 0
    
    res = 0
    if cnt[0] == 1:
        res += dp[-1][0] * pow(2,mod-2,mod)
        res %= mod
        
    return sum(dp[-1]) % mod

ex_q = pow(2,q*(k-1),mod)
ans = calc([0,0,1]) * ex_q % mod
if s[-1] == '0':
    ans += (calc([1,0,0]) * ex_q % mod) * (k-1) % mod
elif s[-1] == '1':
    ans += (calc([0,1,0]) * ex_q % mod) * (k-1) % mod
else:
    ans += (calc([1,0,0]) * ex_q % mod) * (k-1) % mod
    ans += (calc([0,1,0]) * ex_q % mod) * (k-1) % mod
ans %= mod
print(ans)

print(calc([1,0,0]))
print(calc([0,1,0]))
print(calc([0,0,1]))




# dp = [[0,0] for _ in range(l+1)]
# cnt = [1,0,0]
# for i in range(l):
#     if s[i] == '0':
#         dp[i+1][0] = (dp[i][0] + dp[i][1] + cnt[1]) % mod
#         cnt[0] += cnt[1]
#         cnt[0] %= mod
#         cnt[1] = 0
#     elif s[0] == '1':
#         dp[i+1][1] = (dp[i][0] + dp[i][1] + cnt[0]) % mod
#         cnt[1] += cnt[0]
#         cnt[1] %= mod
#         cnt[0] = 0
#     else:
#         dp[i+1][0] = (dp[i][0] + dp[i][1] + cnt[1]) % mod
#         dp[i+1][1] = (dp[i][0] + dp[i][1] + cnt[0]) % mod
#         cnt[0] = (cnt[0] + cnt[1]) % mod
#         cnt[1] = cnt[0]

# print(dp[-1])

# dp = [[0,0] for _ in range(l+1)]
# cnt = [0,1]
# for i in range(l):
#     if s[i] == '0':
#         dp[i+1][0] = (dp[i][0] + dp[i][1] + cnt[1]) % mod
#         cnt[0] += cnt[1]
#         cnt[0] %= mod
#         cnt[1] = 0
#     elif s[0] == '1':
#         dp[i+1][1] = (dp[i][0] + dp[i][1] + cnt[0]) % mod
#         cnt[1] += cnt[0]
#         cnt[1] %= mod
#         cnt[0] = 0
#     else:
#         dp[i+1][0] = (dp[i][0] + dp[i][1] + cnt[1]) % mod
#         dp[i+1][1] = (dp[i][0] + dp[i][1] + cnt[0]) % mod
#         cnt[0] = (cnt[0] + cnt[1]) % mod
#         cnt[1] = cnt[0]

# print(dp[-1])