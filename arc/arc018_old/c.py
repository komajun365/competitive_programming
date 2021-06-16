# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,m = map(int,input().split())
x0,a,p = map(int,input().split())

# for i in range(2,p):
#     if(i**2 > p):
#         break
#     if(p%i==0):
#         print('not prime')
#         exit()

if(a%p==0):
    x1 = (x0+a)%p
    ans = 0
    if(x0!=x1):
        ans = (n-1)*2
    print(ans)
    exit()

score = [[0,0] for _ in range(n*m)]
score[0][0] = x0
x = x0
for i in range(1,n*m):
    x = (x+a)%p
    score[i] = [x,i]

score.sort()
ans = 0
for i in range(n):
    col = []
    for j in range(m):
        _,num = score[i*m+j]
        ans += abs(num//m - i)
        col.append(num%m)

    col.sort()
    for j,c in enumerate(col):
        ans += abs(c-j)

print(ans)




'''
201310

成績が同じ人がいますね・・・
→問題文がバグっているという噂。
'''
