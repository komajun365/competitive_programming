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

# n = 10**3
# mod = 10**9 + 7
# isu = [1] * (n+1)
# for i in range(2,n+1):
#     x = i
#     while x != 1:
#         x = x*i % mod
#         isu[i] += 1

# print(isu[:100])

mod = 10**9 + 7
print(pow(5,mod-2,mod))
print(pow(5,mod-1,mod))

print(pow(5,(mod-1)//2,mod))