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

inf = 10**10

class Seg_min():
    def __init__(self,x):
        #####単位元######
        self.ide_ele_min = inf
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

n,q,*query = list(map(int,read().split()))

wall_ns = Seg_min([inf] * (n-2))
wall_ew = Seg_min([inf] * (n-2))
min_ns = [n-2] * (q+1)
min_ew = [n-2] * (q+1)

ans = (n-2)*(n-2)
for i in range(1,q+1):
    x = query[i*2-1] - 2
    if(query[i*2-2] == 1):
        last = wall_ns.query(0,x)
        if(last == inf):
            last = i-1
        ans -= min_ew[last]

        wall_ns.update(x,i)
        min_ns[i] = min(min_ns[i-1], x)
        min_ew[i] = min_ew[i-1]
    else:
        last = wall_ew.query(0,x)
        if(last == inf):
            last = i-1
        ans -= min_ns[last]

        wall_ew.update(x,i)
        min_ew[i] = min(min_ew[i-1], x)
        min_ns[i] = min_ns[i-1]

print(ans)
