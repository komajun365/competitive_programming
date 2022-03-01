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

tot = sum(a)
a2 = a * 2

r = 0
now = 0
for l in range(n):
    while now * 10 < tot:
        now += a2[r]
        r += 1
    if now * 10 == tot:
        print('Yes')
        exit()
    now -= a2[l]

print('No')


