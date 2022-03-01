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

a = list(map(int,input().split()))
x = a[1] - a[0]
y = a[2] - a[1]
ans = 0
if x < y:
    cnt = (y-x + 1) //2
    y -= cnt
    x += cnt
    ans += cnt
if x > y:
    ans += x-y
print(ans)