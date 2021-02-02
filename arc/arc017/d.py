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
from math import gcd

n = int(readline())
a = list(map(int,readline().split()))
m = int(readline())
tlr = list(map(int,read().split()))

class Seg_gcd():
    def __init__(self,x):
        #####単位元######
        self.ide_ele = 0
        self.func = gcd

        self.n = len(x)

        #num_max:n以上の最小の2のべき乗
        self.num_max =2**(self.n-1).bit_length()
        self.x = [self.ide_ele]*2*self.num_max


        for i,num in enumerate(x, self.num_max):
            self.x[i] = num
        for i in range(self.num_max-1,0,-1):
            self.x[i] = self.func(self.x[i<<1],self.x[(i<<1) + 1])

    def add(self,i,x):
        i += self.num_max
        self.x[i] += x
        while(i>0):
            i = i//2
            self.x[i] = self.func(self.x[i<<1],self.x[(i<<1) + 1])

    def query(self,i,j):
        res = self.ide_ele
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

class Seg_sum():
    def __init__(self,x):
        #####単位元######
        self.ide_ele = 0
        def add(a,b):
            return a+b
        self.func = add

        self.n = len(x)

        #num_max:n以上の最小の2のべき乗
        self.num_max =2**(self.n-1).bit_length()
        self.x = [self.ide_ele]*2*self.num_max


        for i,num in enumerate(x, self.num_max):
            self.x[i] = num
        for i in range(self.num_max-1,0,-1):
            self.x[i] = self.func(self.x[i<<1],self.x[(i<<1) + 1])

    def add(self,i,x):
        i += self.num_max
        self.x[i] += x
        while(i>0):
            i = i//2
            self.x[i] = self.func(self.x[i<<1],self.x[(i<<1) + 1])

    def query(self,i,j):
        res = self.ide_ele
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


a_dif = [0] * (n)
a_dif[0] = a[0]
for i in range(1,n):
    a_dif[i] = a[i]-a[i-1]
a_dif += [0,0,0,0] # 番兵

st = Seg_gcd(a_dif)
st_sum = Seg_sum(a_dif)

ans = []
for i in range(m):
    t,l,r = tlr[i*3:i*3+3]
    if(t==0):
        head = st_sum.query(0,l)
        num = gcd(head, st.query(l,r))
        ans.append(num)
    else:
        st.add(l-1,t)
        st.add(r,t*-1)
        st_sum.add(l-1,t)
        st_sum.add(r,t*-1)

print('\n'.join(map(str,ans)))


'''
遅延評価セグ木だ・・・

と思ったけどよくわからん。
ユークリッドの互除法は
(x,y)　→　(x,y-x) に変換している？
区間への和であれば、y-xは一定。

gcd(a,b,c,d) = gcd(a,b-a,c-b,d-c)だそうです。
l-r にt追加した場合は、
l-k => += t
s-r => -= t

これでよさげ。
あとはセグ木。

だめです。
例えばb~dのgcdを得るとき、
b-aはそのまま使えなくて
そこだけbに置き換える必要があります。

累積和を管理するセグ木をもう一本はやしましょう。


'''
