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
s = input()
mod = 10**9 + 7

cnt = [0] * 8
d = dict()
for i,ch in enumerate('atcoder'):
    d[ch] = i

cnt[0] = 1
for si in s:
    if si in d:
        j = d[si]
        cnt[j+1] += cnt[j]
        cnt[j+1] %= mod

print(cnt[-1])

