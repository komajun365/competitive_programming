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

it = iter(ab)
links = [[] for _ in range(n)]
for a,b in zip(it,it):
    a -= 1
    b -= 1
    links[a].append(b)
    links[b].append(a)

ans = 0

def dfs(bit,i):
    dep = [-1] * n
    dep[i] = 0
    stack = [i]
    while stack:
        j = stack.pop()
        for k in links[j]:
            if (bit >> k) & 1:
                continue
            if dep[k] != -1:
                if dep[k] == dep[j]:
                    return 0
                continue
            done[k] = 1
            dep[k] = 1 - dep[j]
            stack.append(k)
    return 2

def calc(bit):
    res = 3
    for i in range(n):
        if done[i] == 1:
            continue
        done[i] = 1

        if (bit >> i) & 1:
            for j in links[i]:
                if (bit >> j) & 1:
                    return 0
            continue

        tmp = dfs(bit,i)
        res *= tmp
        # if res > 0:
        #     print(bit)
    return res


for bit in range(1<<(n-1)):
    bit = bit*2 + 1
    done = [0] * n
    ans += calc(bit)

print(ans)
