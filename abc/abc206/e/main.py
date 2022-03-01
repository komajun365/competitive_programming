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

l,r = map(int,input().split())
l = max(2,l)
ans = 0
coef = [0] * (r+1)

for i in range(2,r+1):
    add = 1 - coef[i]
    ans += ((r//i) - ((l-1)//i)) ** 2 * add
    for j in range(i*2, r+1, i):
        coef[j] += add

for i in range(l,r+1):
    ans -= r//i * 2
ans += r-l+1
print(ans)