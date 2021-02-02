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
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,*ab = map(int,read().split())
links = [[] for _ in range(n)]
deg = [0] * n

it = iter(ab)
for a,b in zip(it,it):
    a -= 1
    b -= 1
    links[a].append(b)
    links[b].append(a)
    deg[a] += 1
    deg[b] += 1

odd = 0
for di in deg:
    if di % 2 == 1:
        odd += 1

A = (odd+1)//2

root = 1
tp = [root]
stack = [root]
parent = [-1] * n
while(stack):
    i = stack.pop()
    for j in links[i]:
        if j == parent[i]:
            continue
        parent[j] = i
        stack.append(j)
        tp.append(j)

tp = tp[::-1]

def check(x):
    nums = [[] for _ in range(n+1)]
    for i in tp[:-1]:
        if len(nums[i]) % 2 == 0:
            nums[i].append(0)
        num = sorted(nums[i])
        l = len(num)
        if(l == 1):
            next = num[0]
        else:
            rem = [x] * (l//2)
            next = -1
            for j in range(l//2):
                rem[l//2 - 1 - j] -= num[-1-j]
            
            j = l//2
            r = 0
            while(r < l//2):
                if rem[r] >= num[j]:
                    j -= 1
                    r += 1
                else:
                    if next != -1:
                        return False
                    next = num[j]
                    j -= 1
            if next == -1:
                next = num[0]
        next += 1
        if i == tp[-1]:
            next -= 1
        if next > x:
            return False
        nums[parent[i]].append(next)
    print(nums)

    num = sorted(nums[tp[-1]])
    if len(num) % 2 == 1:
        num.pop()
    for i in range(len(num)):
        if num[i] + num[-1-i] > x:
            return False

    return True

# print(tp)
# print(parent)

ok = n
ng = 0
while(ok - ng > 1):
    mid = (ok + ng)//2
    # print(ok,ng,mid,check(mid))
    if check(mid):
        ok = mid
    else:
        ng = mid

print('{} {}'.format(A,ok))


