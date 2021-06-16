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

n,*data = map(int,read().split())
c = data[:n]
ab = data[n:]

links = [[] for _ in range(n)]
it = iter(ab)
for a,b in zip(it,it):
    a -= 1
    b -= 1
    links[a].append(b)
    links[b].append(a)

stack = [0]
cnt = [0] * (10**5 + 1)
ans = [-1] * n
while stack:
    i = stack.pop()
    if i >= 0:
        stack.append(~i)
        ci = c[i]
        if cnt[ci] == 0:
            ans[i] = 1
        else:
            ans[i] = 0
        cnt[ci] += 1
        for j in links[i]:
            if ans[j] != -1:
                continue
            stack.append(j)
    else:
        i = ~i
        ci = c[i]
        cnt[ci] -= 1

ans2 = []
for i in range(n):
    if ans[i] == 1:
        ans2.append(i+1)

print('\n'.join(map(str,ans2)))


