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

n,q,*lr = map(int,read().split())

links = [[] for _ in range(n+1)]
it = iter(lr)
for li,ri in zip(it,it):
    li -= 1
    links[li].append(ri)
    links[ri].append(li)

stack = [0]
done = [0] * (n+1)
while stack:
    x = stack.pop()
    done[x] = 1
    for y in links[x]:
        if done[y] == 1:
            continue
        stack.append(y)

if done[-1] == 1:
    print('Yes')
else:
    print('No')