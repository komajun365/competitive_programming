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

h,w,x,y = map(int,input().split())
s = [input() for _ in range(h)]
x -= 1
y -= 1

ans = 1
for a in [1,-1]:
    for i in range(1,h):
        i *= a
        i += x
        if i < 0 or i >= h:
            break
        if s[i][y] == '#':
            break
        ans += 1

for a in [1,-1]:
    for i in range(1,w):
        i *= a
        i += y
        if i < 0 or i >= w:
            break
        if s[x][i] == '#':
            break
        ans += 1

print(ans)