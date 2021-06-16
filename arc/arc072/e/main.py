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

n,D = map(int,input().split())
d = list(map(int,input().split()))
Q = int(input())
q = list(map(int,input().split()))

point = [D]
for di in d:
    tmp = abs(point[-1] - di)
    point.append( min(tmp, point[-1]) )

reach = [0] * (n+1)
for i in range(n-1,-1,-1):
    if d[i] <= reach[i+1]*2+1:
        reach[i] = reach[i+1] + d[i]
    else:
        reach[i] = reach[i+1]

ans = []
for qi in q:
    if point[qi-1] <= reach[qi]:
        ans.append('NO')
    else:
        ans.append('YES')

print('\n'.join(ans))