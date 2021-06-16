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

links = [[] for _ in range(n)]
it = iter(ab)
for a,b in zip(it,it):
    a -= 1
    b -= 1
    links[a].append(b)
    links[b].append(a)

stack = [0]
parent = [-1] * n
size = [1] * n
c_size = [[] for _ in range(n)]
while stack:
    i = stack.pop()
    if i >= 0:
        stack.append(~i)
        for j in links[i]:
            if parent[i] == j:
                continue
            stack.append(j)
            parent[j] = i
    else:
        i = ~i
        for j in links[i]:
            if parent[i] == j:
                continue
            size[i] += size[j]
            c_size[i].append((size[j] << 20) + j)

base = (1<<20)-1
ans = [-1] * n
num = 0
stack = [0]
tp = []
while stack:
    i = stack.pop()
    tp.append(i)
    num += 1
    if i >= 0:
        stack.append(~i)
        c_size[i].sort(reverse=True)
        for x in c_size[i]:
            j = x & base
            stack.append(j)
    else:
        i = ~i
        if len(c_size[i]) > 0:
            tmp = 10**10
            for x in c_size[i]:
                j = x & base
                tmp = min(tmp,ans[j])
            ans[i] = tmp+1
        else:
            ans[i] = num
    # print(num,ans)

min_n = min(ans)
ans = [i - min_n + 1 for i in ans]

print(' '.join(map(str,ans)))
# print(tp)

