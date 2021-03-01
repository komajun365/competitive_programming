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

# 最大長方形のアルゴリズムを使う

import sys
read = sys.stdin.read

h,w,*s = read().split()
h = int(h)
w = int(w)

paint = [[0] * (w-1) for _ in range(h-1)]
for i in range(h-1):
    for j in range(w-1):
        cnt = 0
        for x in [i,i+1]:
            for y in [j,j+1]:
                if s[x][y] == '.':
                    cnt += 1
        if cnt % 2 == 0:
            paint[i][j] = 1

for j in range(w-1):
    for i in range(h-3,-1,-1):
        if paint[i][j] != 0:
            paint[i][j] += paint[i+1][j]

ans = max(h,w)
for i in range(h-1):
    stack = [[0,-1]]
    for j in range(w):
        if j == w-1:
            num = 0
        else:
            num = paint[i][j]
        idx = j
        while stack:
            if(stack[-1][0] > num):
                x,idx  = stack.pop()
                if x == 0:
                    continue
                ans = max(ans, (x+1) * (j-idx+1))
            else:
                break
        stack.append([num,idx])

print(ans)


# print(paint)
