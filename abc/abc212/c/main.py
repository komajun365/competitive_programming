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

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ab = []
for ai in a:
    ab.append([ai,0])
for bi in b:
    ab.append([bi,1])

ab.sort()
ans = 10**10
for i in range(n+m-1):
    if ab[i][1] + ab[i+1][1] == 1:
        ans = min(ans, ab[i+1][0] - ab[i][0])

print(ans)