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

# def sieve(n):
#     if( n <= 1):
#         return []
#     elif(n==2):
#         return [2]

#     primes = [2]
#     len_list = (n+1)//2
#     len_sqrt = int(len_list**0.5) + 1
#     flags = [True] * len_list
#     flags[0] = False
#     for i in range(len_sqrt):
#         if(flags[i]):
#             start = ((i*2+1)**2)//2
#             for j in range( start, len_list, i*2+1):
#                 flags[j] = False
#     return [2] + [i*2+1 for i in range(len_list) if flags[i]]

a,b = map(int,input().split())

n = b-a+1
if n == 1:
    print(2)
    exit()

ans = 0
# if a == 1:
#     ans += 1
#     a += 1
#     n -= 1

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
while primes:
    if primes[-1] > n:
        primes.pop()
    else:
        break
l = len(primes)

bits = [0] * n
for i in range(n):
    x = a+i
    for j,pj in enumerate(primes):
        if x % pj == 0:
            bits[i] += 1 << j

dp = [0] * (1<<l)
dp[0] = 1
for i in range(n):
    dp2 = [0] * (1<<l)
    for j in range(1<<l):
        if dp[j] == 0:
            continue
        dp2[j] += dp[j]
        if j & bits[i] == 0:
            dp2[j | bits[i]] += dp[j]
    dp,dp2 = dp2,dp

ans += sum(dp)
print(ans)

# print(primes)

