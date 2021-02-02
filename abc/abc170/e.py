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

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from heapq import heappop,heappush

class Seg_min():
    def __init__(self,x):
        #####単位元######
        self.ide_ele_min = 10**10
        self.func = min

        self.n = len(x)

        #num_max:n以上の最小の2のべき乗
        self.num_max =2**(self.n-1).bit_length()
        self.x = [self.ide_ele_min]*2*self.num_max

        for i,num in enumerate(x, self.num_max):
            self.x[i] = num
        for i in range(self.num_max-1,0,-1):
            self.x[i] = self.func(self.x[i<<1],self.x[(i<<1) + 1])

    def update(self,i,x):
        i += self.num_max
        self.x[i] = x
        while(i>0):
            i = i//2
            self.x[i] = self.func(self.x[i<<1],self.x[(i<<1) + 1])

    def query(self,i,j):
        res = self.ide_ele_min
        if i>=j:
            return res
        i += self.num_max
        j += self.num_max -1
        while(i<=j):
            if(i==j):
                res = self.func(res,self.x[i])
                break
            if(i&1):
                res = self.func(res,self.x[i])
                i += 1
            if(not j&1):
                res = self.func(res,self.x[j])
                j -= 1
            i = i>>1
            j = j>>1
        return res

n,q = map(int,readline().split())
data = list(map(int,read().split()))
a = data[:2*n:2]
b = data[1:2*n:2]
c = data[2*n::2]
d = data[2*n+1::2]

m = 2*10**5

hq_kinder =[[] for _ in range(m+1)]
hq_gone =[[] for _ in range(m+1)]

for ai,bi in zip(a,b):
    heappush(hq_kinder[bi], ai*-1)

x = [10**10] * (m+1)
for i,hq in enumerate(hq_kinder[1:],1):
    if(hq):
        x[i] = hq[0] * -1

seg = Seg_min(x)

ans = []
for ci,di in zip(c,d):
    ci_rate = a[ci-1]
    ci_before = b[ci-1]
    heappush(hq_gone[ci_before], ci_rate*-1)

    b[ci-1] = di
    heappush(hq_kinder[di], ci_rate*-1)

    # update
    for j in [ci_before,di]:
        while(hq_gone[j]):
            if(hq_kinder[j][0] == hq_gone[j][0]):
                heappop(hq_kinder[j])
                heappop(hq_gone[j])
            else:
                break
        if(hq_kinder[j]):
            seg.update(j,hq_kinder[j][0]*-1)
        else:
            seg.update(j,10**10)

    ans.append(seg.x[1])

print('\n'.join(map(str,ans)))
