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

n,q,*data = map(int,read().split())
x = data[:n]
ab = data[n:n*3-2]
vk = data[n*3-2:]

links = [[] for _ in range(n)]
it = iter(ab)
for ai,bi in zip(it,it):
    ai -= 1
    bi -= 1
    links[ai].append(bi)
    links[bi].append(ai)

order = []
parent = [-1] * n
parent[0] = -2
stack = [0]
while stack:
    i = stack.pop()
    order.append(i)
    for j in links[i]:
        if parent[j] != -1:
            continue
        parent[j] = i
        stack.append(j)

ans = [-1] * q
que = [[] for _ in range(n)]
for i in range(q):
    vi,ki = vk[2*i:2*i+2]
    vi -= 1
    ki -= 1
    que[vi].append((i,ki))

nums = [[xi] for xi in x]
def join(i,j):
    res = []
    i_idx = 0
    j_idx = 0
    i_len = len(nums[i])
    j_len = len(nums[j])
    for _ in range(20):
        if i_idx == i_len and j_idx == j_len:
            break
        elif i_idx == i_len:
            res.append(nums[j][j_idx])
            j_idx += 1
        elif j_idx == j_len:
            res.append(nums[i][i_idx])
            i_idx += 1
        elif nums[i][i_idx] > nums[j][j_idx]:
            res.append(nums[i][i_idx])
            i_idx += 1
        else:
            res.append(nums[j][j_idx])
            j_idx += 1
    return res

for i in order[::-1]:
    for idx,ki in que[i]:
        ans[idx] = nums[i][ki]
    if i != 0:
        p = parent[i]
        nums[p] = join(i,p)

print(*ans, sep='\n')

