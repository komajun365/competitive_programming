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

n,*vw = map(int,read().split())
if n == 2:
    print('1 2')
    exit()
elif n == 3:
    print('1 2 3')
    exit()

links = [set() for _ in range(n)]
deg = [0] * n

it = iter(vw)
for v,w in zip(it,it):
    v -= 1
    w -= 1
    links[v].add(w)
    links[w].add(v)
    deg[v] += 1
    deg[w] += 1

leaf = []
for i in range(n):
    if deg[i] == 1:
        leaf.append(i)

l_num = [0] * n
for l in leaf:
    m = links[l].pop()
    links[m].remove(l)
    deg[l] -= 1
    deg[m] -= 1
    l_num[m] += 1

if max(deg) > 2:
    print(-1)
    exit()

head = -1
for i in range(n):
    if deg[i] == 1:
        head = i
        break

if head == -1:
    nums = [ max(l_num) ]
else:
    nums = [l_num[head]]
    i = head
    while links[i]:
        j = links[i].pop()
        links[j].remove(i)
        i = j
        nums.append(l_num[i])

nums_r = nums[::-1]
ans1,ans2 = [],[]
for x,ans in zip([nums, nums_r],[ans1,ans2]):
    ans.append(1)
    x[0] -= 1
    x[-1] -= 1
    now = 1
    for i in x:
        for j in range(now+2,now+2+i):
            ans.append(j)
        ans.append(now+1)
        now += 1+i
    ans.append(n)

ans = ans1[::]
for a1,a2 in zip(ans1,ans2):
    if a1 > a2:
        ans = ans2[::]
        break
    elif a1 < a2:
        break
print(' '.join(map(str,ans)))


# ans = []
# for i in range(nums[0] + 1):
#     ans.append(i+1)
# nums[-1] -= 1
# now = nums[0] + 1

# for i in nums[1:]:
#     for j in range(now+2,now+2+i):
#         ans.append(j)
#     ans.append(now+1)
#     now += 1+i
# ans.append(n)

# print(' '.join(map(str,ans)))



