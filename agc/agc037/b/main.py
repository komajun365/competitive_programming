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
mod = 998244353

d = {'R':1, 'G':2, 'B':4}
ans = 1
stock = [0] * 8
for si in s:
    x = d[si]
    if stock[7-x] > 0:
        ans *= stock[7-x]
        ans %= mod
        stock[7-x] -= 1
    else:
        for y in [1,2,4]:
            if y == x:
                continue
            if stock[y] > 0:
                ans *= stock[y]
                ans %= mod
                stock[y] -= 1
                stock[x+y] += 1
                break
        else:
            stock[x] += 1

for i in range(1,n+1):
    ans *= i
    ans %= mod
print(ans)

