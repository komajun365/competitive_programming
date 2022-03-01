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

p = int(input())
ans = 0
coin = 1
for i in range(1,11):
    coin *= i
for i in range(10,0,-1):
    num = min(100, p//coin)
    ans += num
    p -= coin*num
    coin //= i
print(ans)