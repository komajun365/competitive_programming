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

h,w,d = map(int,input().split())

ans = [[''] * w for _ in range(h)]
if d % 2 == 1:
    for i in range(h):
        for j in range(w):
            if (i+j)%2 == 0:
                ans[i][j] = 'R'
            else:
                ans[i][j] = 'G'
else:
    for i in range(h):
        for j in range(w):
            x = ((i+j) //2) % d
            y = ((i-j) //2) % d
            if x < d//2 and y < d//2:
                ans[i][j] = 'R'
            elif x < d//2 and y >= d//2:
                ans[i][j] = 'G'
            elif x >= d//2 and y >= d//2:
                ans[i][j] = 'B'
            else:
                ans[i][j] = 'Y'
print('\n'.join(map(lambda x:''.join(x),ans)))