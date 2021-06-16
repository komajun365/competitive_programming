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
import bisect

n,m,*data = map(int,read().split())

ab = []
for i in range(n):
    a,b = data[i*2:i*2+2]
    ab.append([-1*a,b])

ab.sort()
a_list = [a for a,_ in ab]
b_list = [b for _,b in ab]

lr = [[] for _ in range(n)]
for i in range(n,n+m):
    r,l = data[i*2:i*2+2]
    l *= -1
    r *= -1
    l = bisect.bisect_left(a_list, l)
    r = bisect.bisect_right(a_list, r)
    if l != r:
        lr[l].append([r,i-n])

use = [0] * m
parent = []
state = [0] * (n+1)
tail = m-1
for i in range(n):
    state[i] += state[i-1]
    use_i = (state[i] - b_list[i]) % 2
    if use_i == 1 and len(lr[i]) == 0:
        print(-1)
        exit()
    if len(lr[i]) == 0:
        continue
    lr[i].sort()
    r,idx = lr[i][0]
    if use_i == 1:
        use[idx] += 1
        state[i] += 1
        state[r] -= 1
    for r2,idx2 in lr[i][1:]:
        if r == r2:
            continue
        tail += 1
        use.append(0)
        parent.append([idx,idx2])
        lr[r].append([r2,tail])
        r = r2
        idx = idx2

# print(use)
# print(parent)
# print(state)
# print(b_list)

for i in range(tail,m-1,-1):
    p1,p2 = parent.pop()
    use[p1] += use[i]
    use[p2] += use[i]

ans = []
for i in range(m):
    if use[i] % 2 == 1:
        ans.append(i+1)

print(len(ans))
print(*ans)

# for i in range(n):
#     for r,idx in lr[i]:
#         if idx+1 in ans:
#             print(i,r,idx+1)

# print(b_list)