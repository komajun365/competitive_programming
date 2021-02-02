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
xy = [list(map(int,input().split())) for _ in range(n)]

ans = 0
for i in range(n-1):
    xi,yi = xy[i]
    for j in range(i+1,n):
        xj,yj = xy[j]
        if( xi == xj ):
            continue
        if abs(xi-xj) >= abs(yi-yj):
            ans += 1

print(ans) 
