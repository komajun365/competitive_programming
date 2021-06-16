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

n,m,*ab = map(int,read().split())

links = [[] for _ in range(n)]
it = iter(ab)
for a,b in zip(it,it):
    a -= 1
    b -= 1
    links[a].append(b)

ans = 0
for i in range(n):
    stack = [i]
    done = [0] * n
    done[i] = 1
    ans += 1
    while stack:
        j = stack.pop()
        for k in links[j]:
            if done[k] == 1:
                continue
            done[k] = 1
            ans += 1
            stack.append(k)

print(ans)
