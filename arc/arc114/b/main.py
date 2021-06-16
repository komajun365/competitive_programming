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
f = list(map(int,input().split()))
mod = 998244353

links = [[] for _ in range(2*n)]
for i,fi in enumerate(f):
    fi -= 1
    links[i].append(fi + n)
    links[i+n].append(i)

cnt = 0
use = [-1] * (2*n)
for i in range(n):
    if use[i] >= 0:
        continue
    
    x = i
    while links[x]:
        x = links[x][0]
        if use[x] == -1:
            use[x] = i
        elif use[x] == i:
            cnt += 1
            break
        else:
            break

ans = pow(2,cnt,mod) - 1
ans %= mod
print(ans)

