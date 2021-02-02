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
t = input()
mod = 998244353

s0 = 'keyence'
g = set()
for i in range(2**7):
    tmp = ''
    for j in range(7):
        if (i >> j) & 1:
            tmp += s0[j]
    g.add(tmp)

print(g)
print(len(g))