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
from collections import deque

n,k,*uv = map(int,read().split())

links = [[] for _ in range(n)]
it = iter(uv)
for u,v in zip(it,it):
    u -= 1
    v -= 1
    links[u].append(v)
    links[v].append(u)

root = 0
dq = deque()
dq.append(root)
tp = [root]
parent = [-1] * n
parent[root] = -2

while dq:
    i = dq.popleft()
    for j in links[i]:
        if parent[j] != -1:
            continue
        parent[j] = i
        dq.append(j)
        tp.append(j)

root = tp[-1]
dq = deque()
dq.append(root)
tp = [root]
parent = [-1] * n
parent[root] = -2

while dq:
    i = dq.popleft()
    for j in links[i]:
        if parent[j] != -1:
            continue
        parent[j] = i
        dq.append(j)
        tp.append(j)

tp = tp[::-1]

def check(x):
    cnt = 0
    done = [0] * n
    rem = [-1] * n
    for i in tp:
        # print(x,i,cnt,done,rem)
        if done[i] == 1:
            continue

        p = i
        for up in range(x):
            if up <= rem[p]:
                break
            if parent[p] == -2:
                stack = [p]
                nums = dict()
                nums[p] = up
                while stack:
                    a = stack.pop()
                    for b in links[a]:
                        if b in nums:
                            continue
                        nums[b] = nums[a] + 1
                        if nums[b] <= rem[b]:
                            return True
                        if nums[b] < x:
                            stack.append(b)
                cnt += 1
                if cnt <= k:
                    return True
                else:
                    return False

            p = parent[p]
        else:
            rem[p] = x
            cnt += 1
        if cnt > k:
            return False

        stack = [p]
        while stack:
            a = stack.pop()
            done[a] = 1
            if rem[a] == 0:
                continue
            for b in links[a]:
                if done[b] == 1:
                    continue
                if b == parent[p]:
                    rem[b] = rem[p] - 1
                    continue
                rem[b] = rem[a] - 1
                stack.append(b)
    
    return True

ok = n
ng = 0
while ok-ng > 1:
    mid = (ok+ng)//2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)

