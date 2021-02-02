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

r1,c1 = map(int,input().split())
r2,c2 = map(int,input().split())

ans = 3
if(r1==r2) and (c1==c2):
    ans = min(ans,0)

if(r1+c1 == r2+c2) or (r1-c1 == r2-c2) or (abs(r2-r1) + abs(c2-c1) <= 3):
    ans = min(ans,1)

for dx in range(-3,4):
    for dy in range(-3,4):
        if(abs(dx)+abs(dy)) > 3:
            continue
        r = r1 + dx
        c = c1 + dy
        if(r==r2) and (c==c2):
            ans = min(ans,1)
        if(r+c == r2+c2) or (r-c == r2-c2) or (abs(r2-r) + abs(c2-c) <= 3):
            ans = min(ans,2)

if(r2+c2-r1-c1)%2 == 1:
    ans = min(ans,3)
else:
    ans = min(ans,2)

print(ans)

