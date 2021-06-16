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

a,b,c = map(int,input().split())
ans = a*b*c
for _ in range(3):
    x = a//2
    y = (a+1)//2
    ans = min(ans, (y-x)*b*c)
    a,b,c = b,c,a

print(ans)