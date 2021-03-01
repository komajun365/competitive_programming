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

# import time
# start = time.time()

import sys,random
f=random.randint
n,m,k,*c=map(int,sys.stdin.buffer.read().split())
t=280000
b=t
for _ in range(t):
 l=list(range(n))
 for z in range(k):
  i=f(0,n-1)
  j=(f(1,n-1)+i)%n
  l[i],l[j]=l[j],l[i]
 it=iter(c)
 for x,y in zip(it,it):
  if not 1<abs(l[x]-l[y])<n-1:
   b-=1
   break
print(b/t)
# print(b,t)

# while( time.time() - start < 9.5):
#     for _ in range(100):
#         l = list(range(n))
#         for ki in range(k):
#             i = randint(0,n-1)
#             j = (randint(1,n-1) + i) % n
#             l[i],l[j] = l[j],l[i]
#         it = iter(ab)
#         for a,b in zip(it,it):
#             dif = abs(l[a] - l[b])
#             if dif == 1 or dif == n-1:
#                 bad -= 1
#                 break
# print(1 - bad/tot)
