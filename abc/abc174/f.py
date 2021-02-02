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

class Seg_sum():
    def __init__(self,x):
        #####単位元######
        self.ide_ele_min = 0
        self.func = lambda a,b : a+b

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
c = tuple(map(int,readline().split()))
lr = tuple(map(int,read().split()))
it = iter(lr)
lrq = [[] for _ in range(n)]
for i,l,r in zip(range(q),it,it):
    lrq[r-1].append((l-1,i))

st = Seg_sum([1]*(n+1))
ans = [0] * q
before = [-1] * (n+1)
c_ind = 0
for r in range(n):
    for l,i in lrq[r]:
        while(c_ind <= r):
            bef = before[c[c_ind]]
            if(bef!=-1):
                st.update(bef,0)
            before[c[c_ind]] = c_ind
            c_ind += 1

        ans[i] = st.query(l,r+1)

print('\n'.join(map(str,ans)))




# hoge = list(range(10**5))
# for _ in range(4):
#     hoge += list(range(10**5))
#
# hoge.sort()
