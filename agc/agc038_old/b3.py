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

n,k = map(int,input().split())
p = tuple(map(int,input().split()))

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
        while(x>0):
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

class Seg_max():
    def __init__(self,x):
        #####単位元######
        self.ide_ele_min = 10**10 * -1
        self.func = max

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
        while(x>0):
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

seg_min = Seg_min(p)
seg_max = Seg_max(p)

natural = 0
ans = 0

head = 0
for i in range(1,n):
    if(p[i]<p[i-1]):
        head = i

    if(i-head >= k-1):
        natural = 1
        continue

    if(i==k-1):
        ans +=1
    if(i<k):
        continue
    ans += 1

    left = seg_min.query(i-k,i)
    right = seg_max.query(i-k+1,i+1)
    if(left==p[i-k])&(right==p[i]):
        ans -= 1

print(ans+natural)
# print(ans,natural)

'''

(0,k-1)
(1,k)
が同じ条件は
min(0-k-1) = (0)
max(1-k) = (k)

ただし、k個昇順のままならとびとびのｋでも同じになるのでそれは除外する。

せっかくなので最小値最大値はBITで行きましょう
'''
