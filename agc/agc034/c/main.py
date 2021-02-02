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

n,x,*data = map(int,read().split())

it = iter(data)
blu = [[b,l,u, l*b + u*(x-b)] for b,l,u in zip(it,it,it)]
blu.sort(key = lambda a: -1 * a[3])

aoki = 0
for b,l,u,_ in blu:
    aoki += b*l

cs = [0]
use = -1
for i in range(n):
    cs.append(cs[-1] + blu[i][3])
    if use==-1 and cs[-1] >= aoki:
        use = i

# print(cs)
# print(use,aoki)

ans = n*x
for i in range(n):
    if i < use:
        tak = cs[use+1] - blu[i][3]
    else:
        tak = cs[use]
    rem = aoki - tak
    b,l,u,_ = blu[i]
    tmp = use*x
    if(b*l >= rem):
        tmp += -((-rem)//l)
    else:
        tmp += b
        rem -= b*l
        tmp += -((-rem)//u)
    ans = min(ans,tmp)

print(ans)





# ok = n*x
# ng = -1
# while(ok-ng > 1):
#     mid = (ok+ng)//2
#     rem = mid
#     tak = 0
#     i = 0
#     while(rem >= x):
#         tak += blu[i][3]
#         rem -= x
#         i += 1
#     last = 0
#     if(rem != 0):
#         for j in range(n):
#             b,l,u,lim = blu[j]
#             if( lim <= blu[i][3]):
#                 tmp = l * min(rem,b) + u * max(0, rem-b)
#                 last = max(tmp,last)
#     tak += last

#     if(tak >= aoki):
#         ok = mid
#     else:
#         ng = mid

# print(ok)

# print(blu)