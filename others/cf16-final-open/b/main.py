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
tot = 0
for i in range(1,10**4):
    tot += i
    if tot > n:
        break
dif = tot - n
ans = []
for j in range(1,i+1):
    if j != dif:
        ans.append(j)
print('\n'.join(map(str,ans)))