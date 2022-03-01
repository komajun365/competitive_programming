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

links = [[] for _ in range(n+1)]
it = iter(ab)
for a,b in zip(it,it):
    links[a].append(b)
    links[b].append(a)

for i in range(n+1):
    links[i].sort(reverse=True)

ans = []
done = [0] * (n+1)
stack = [1]
while stack:
    i = stack.pop()
    if i > 0:
        ans.append(i)
        done[i] = 1
        for j in links[i]:
            if done[j] == 1:
                continue
            stack.append(-i)
            stack.append(j)
    else:
        ans.append(-i)

print(' '.join(map(str,ans)))

    