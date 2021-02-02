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
x = list(map(int,input().split()))
xs = sorted(x)
l = xs[n//2-1]
r = xs[n//2]
ans = []
for xi in x:
    if xi <= l:
        ans.append(r)
    else:
        ans.append(l)
print(*ans, sep='\n')
