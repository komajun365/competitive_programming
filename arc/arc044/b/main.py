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
mod = 10**9 + 7

if a[0] != 0:
    print(0)
    exit()


cnt = [0] * (n+1)
for ai in a:
    cnt[ai] += 1

if cnt[0] != 1:
    print(0)
    exit()

ans = 1
for i in range(n):
    p = cnt[i]
    c = cnt[i+1]
    if p == 0 and c > 0:
        print(0)
        exit()
    if c == 0:
        continue
    ans *= pow(pow(2,p,mod) - 1, c, mod)
    ans %= mod
    ans *= pow(2,c*(c-1)//2,mod)
    ans %= mod

print(ans)
    