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
from math import log2

class Seg_sum():
    def __init__(self,x):
        #####単位元######
        self.ide_ele_min = 0.0
        self.func = lambda x,y: x+y

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

n = int(readline())
data = list(map(int,read().split()))
it = iter(data[:2*n])
pq = [[p,q] for p,q in zip(it,it)]
q = data[2*n]
query = data[2*n+1:]

fac = [0.0] *  (10**6+5)
for i in range(1,10**6+5):
    fac[i] = fac[i-1] + log2(i)

def com(n,k):
    res = fac[n] - fac[k] - fac[n-k]
    return res

origin = [0.0] * n
for i in range(1,n):
    c1 = sum(pq[i]) - sum(pq[i-1])
    c2 = pq[i][0] - pq[i-1][0]
    origin[i] = com(c1,c2)

st = Seg_sum(origin)

ind = 0
ans = []
for _ in range(q):
    if(query[ind] == 1):
        k,a,b = query[ind+1:ind+4]
        ind += 4
        pq[k-1] = [a,b]
        for i in range(max(1,k-1),min(k+1,n)):
            c1 = sum(pq[i]) - sum(pq[i-1])
            c2 = pq[i][0] - pq[i-1][0]
            st.update(i,com(c1,c2))
    else:
        l1,r1,l2,r2 = query[ind+1:ind+5]
        ind += 5
        num1 = st.query(l1,r1)
        num2 = st.query(l2,r2)
        if(num1 > num2):
            ans.append('FIRST')
        else:
            ans.append('SECOND')

if(ans):
    print('\n'.join(ans))





'''
少しの誤差は許されるので、
logで管理すればよいと思われる。

com(n,k) = n! / (k! * (n-k)!)

n! までのlogを持っていればO(1)で更新できそう。

'''
