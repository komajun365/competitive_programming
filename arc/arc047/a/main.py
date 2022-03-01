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

n,l = map(int,input().split())
s = input()

ans = 0
x = 1
for si in s:
    if si == '+':
        x += 1
    else:
        x -= 1
    
    if x > l:
        ans += 1
        x = 1
print(ans)