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
t = input()

s0 = []
t0 = []
for i in range(n):
    if s[i] == '0':
        s0.append(i)
    if t[i] == '0':
        t0.append(i)

if len(s0) != len(t0):
    print(-1)
else:
    ans = 0
    for si,ti in zip(s0,t0):
        if si != ti:
            ans += 1
    print(ans)

