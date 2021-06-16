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

# import sys
# sys.setrecursionlimit(10**9)
# from functools import lru_cache

s = input()

ans = 0
while True:
    idx = s.find('iiwi')
    if idx >= 0:
        s = s[:idx] + 'i' + s[idx+4:]
        ans += 1
        continue
    idx = s.find('iwii')
    if idx >= 0:
        s = s[:idx] + 'i' + s[idx+4:]
        ans += 1
        continue
    break

cnt = 0
want = 0
d = {0:'i', 1:'w'}
for i in range(len(s)):
    if s[i] == d[want]:
        cnt += 1
        want ^= 1
        continue
    ans += (cnt+1)//4
    if s[i] == 'i':
        cnt = 1
        want = 1
    else:
        cnt = 0
        want = 0
else:
    ans += (cnt+1)//4

print(ans)

