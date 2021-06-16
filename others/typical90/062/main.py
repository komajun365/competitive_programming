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

import sys
read = sys.stdin.buffer.read

n,*ab = map(int,read().split())

use = [[] for _ in range(n)]
white = [0] * n
ans = []
stack = []
for i in range(n):
    for x in ab[i*2:i*2+2]:
        x -= 1
        if x == i and white[x] == 0:
            stack.append(x)
            white[x] = 1
            ans.append(x+1)
        else:
            use[x].append(i)

while stack:
    x = stack.pop()
    for y in use[x]:
        if white[y] == 1:
            continue
        white[y] = 1
        ans.append(y+1)
        stack.append(y)

if sum(white) != n:
    print(-1)
else:
    print('\n'.join(map(str, ans[::-1])))
