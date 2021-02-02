import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

m,k = map(int, input().split())

if( k >= 2**m):
    print(-1)
    exit()

if( (m==1) & (k==1) ):
    print(-1)
    exit()


n = 2**(m+1)
ans = [0] * n
if( k==0):
    for i in range(n):
        ans[i] = i//2
    print(' '.join([str(i) for i in ans ]))
    exit()

ans[0] = k
ind = 1
for i in range(n//2):
    if(i != k):
        ans[ind] = i
        ind += 1

ans[ind] = k
ind += 1

for i in range(n//2 -1, -1, -1):
    if(i != k):
        ans[ind] = i
        ind += 1


print(' '.join([str(i) for i in ans ]))

# ###############
# import random
#
# dict = {}
# base = [0,0,1,1,2,2,3,3]
# # xors = [0,0,0,0]
# for _ in range(1000):
#     random.shuffle(base)
#     for i in range(4):
#         head = base.index(i)
#         tail = base[head+1:].index(i) + head + 1
#         tmp = 0
#         for j in range(head+1, tail):
#             tmp = tmp^base[j]
#
#         if(i != 0):
#             if(before != tmp):
#                 break
#         before = tmp
#
#         if(i == 3) & (tmp!=0):
#             print(base)
#             print(tmp)
