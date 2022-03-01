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

s,t = map(int,input().split())

ans = 0
for a in range(s+1):
    for b in range(s+1):
        for c in range(s+1):
            if a+b+c <= s and a*b*c <= t:
                ans += 1
print(ans)