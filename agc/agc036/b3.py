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

import bisect

n,k = map(int,input().split())
a = list(map(int,input().split()))

ind = [[] for _ in range(2*10**5 + 1)]
for i,num in enumerate(a):
    ind[num].append(i)

for i in range(1,2*10**5 + 1):
    if(ind[i]):
        ind[i].append(ind[i][0] + n)

before = []
cnt = 0
now = a[0]
while(True):
    right = bisect.bisect_right(ind[now], cnt%n)
    cnt += ind[now][right] - ind[now][right-1] + 1
    if(ind[now][right] >= n):
        before.append(ind[now][right-1])
    now = a[cnt%n]
    if(cnt%n == 0):
        break

if(cnt//n==1):
    print('')
    exit()

cyc = k%(cnt//n)

cnt = before[cyc-1]
ans = []
while(cnt < n):
    now = a[cnt]
    right = bisect.bisect_right(ind[now],cnt)
    if(ind[now][right] >= n):
        ans.append(now)
        cnt += 1
    else:
        cnt = ind[now][right] + 1

print(' '.join(map(str,ans)))
# print(before)

'''
(1,2,3,2,3)
[]
1,3
3
2,3


'''
