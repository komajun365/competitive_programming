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

n,*uvww = map(int,read().split())
w1s = uvww[2::4]
w2s = uvww[3::4]

links = [[] for _ in range(n)]
it = iter(uvww)
for u,v,w1,w2 in zip(it,it,it,it):
    u -= 1
    v -= 1
    links[u].append([v,w1,w2])
    links[v].append([u,w1,w2])

root = 0
xors1 = [-1] * n
xors2 = [-1] * n
xors1[root] = 0
xors2[root] = 0
stack = [root]
while(stack):
    i = stack.pop()
    for j,w1,w2 in links[i]:
        if xors1[j] != -1:
            continue
        xors1[j] = xors1[i] ^ w1
        xors2[j] = xors2[i] ^ w2
        stack.append(j)


dif = 0
for x1 in xors1:
    dif ^= x1
for x2 in xors2:
    dif ^= x2

def get_base(x,basis):
    for b in basis:
        x = min(x,x^b)
    return x

# basis = []
# for num in xors1:
#     x = get_base(num,basis)
#     if x != 0:
#         basis.append(x)

# # print(dif)
# # print(xors1)
# # print(xors2)

# x = get_base(dif, basis)
# if x != 0:
#     print('NO')
#     exit()

for i in range(n):
    xors1[i] ^= dif

xors1.sort()
xors2.sort()

# print(xors1)
# print(xors2)

if xors1 == xors2:
    print('YES')
else:
    print('NO')

