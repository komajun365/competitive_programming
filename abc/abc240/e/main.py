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

n,*uv = map(int,read().split())

links = [[] for _ in range(n+1)]
it = iter(uv)
for ui,vi in zip(it,it):
    links[ui].append(vi)
    links[vi].append(ui)

stack = [~1,1]
left = [0] * (n+1)
right = [0] * (n+1)
leaf = 0
while stack:
    x = stack.pop()
    if x > 0:
        left[x] = leaf+1
        stack.append(~x)
        for y in links[x]:
            if left[y] == 0:
                stack.append(y)
    else:
        x = ~x
        if len(links[x]) == 1 and x != 1:
            leaf += 1
        right[x] = leaf

ans = []
for i in range(1,n+1):
    ans.append('{} {}'.format(left[i], right[i]))
print(*ans, sep='\n')

