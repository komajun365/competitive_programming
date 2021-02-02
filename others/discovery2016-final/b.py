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

# import copy

class Seg_max():
    def __init__(self,x):
        #####単位元######
        self.ide_ele_min = 10**10 * -1
        def seg_func(a,b):
            if(a[0] >= b[0]):
                return a
            else:
                return b

        self.func = seg_func

        self.n = len(x)

        #num_max:n以上の最小の2のべき乗
        self.num_max =2**(self.n-1).bit_length()
        self.x = [[self.ide_ele_min,i] for i in range(2*self.num_max)]

        for i,(_,num) in enumerate(x, self.num_max):
            self.x[i] = [num,i-self.num_max]
        for i in range(self.num_max-1,0,-1):
            self.x[i] = self.func(self.x[i<<1],self.x[(i<<1) + 1])[::]

    def update(self,i,x):
        i += self.num_max
        self.x[i][0] = x
        while(i>0):
            i = i//2
            self.x[i] = self.func(self.x[i<<1],self.x[(i<<1) + 1])[::]

    def query(self,i,j):
        res = [self.ide_ele_min,-1]
        if i>=j:
            return res
        i += self.num_max
        j += self.num_max -1
        while(i<=j):
            if(i==j):
                res = self.func(res,self.x[i])[::]
                break
            if(i&1):
                res = self.func(res,self.x[i])[::]
                i += 1
            if(not j&1):
                res = self.func(res,self.x[j])[::]
                j -= 1
            i = i>>1
            j = j>>1
        return res

n,x = map(int,input().split())
t = list(map(int,input().split()))
a = list(map(int,input().split()))
ta = [[i,j] for i,j in zip(t,a)]
ta.sort()

inf = n
ind_t = [inf] * (10**5+1)
ind_t[0] = 0
i = 0
for time in range(1,10**5+1):
    if(ta[i][0] > time):
        ind_t[time] = ind_t[time-1]
        continue
    while(ta[i][0] <= time):
        i += 1
        if(i==inf):
            break
    else:
        ind_t[time] = i
    if(i==inf):
        break

ok = n+2
ng = 0
mid = 7*(ok+ng)//16
while(ok-ng>1):
    a_sum = 0
    seg = Seg_max(ta)
    for i in range(mid-1,-1,-1):
        if(ind_t[i] == inf):
            # 料理が一つも残ってない時間
            continue
        num,j = seg.query(ind_t[i],n)
        a_sum += num
        seg.update(j,0)

    if(a_sum >= x):
        ok = mid
    else:
        ng = mid

    mid = (ok+ng)//2

if(ok == n+2):
    print(-1)
else:
    print(ok)





'''
二分探索しましょう。
y秒で美味しさの総和最大化を目指します。
y-1秒でトレーに乗せるべき料理は、その時に取れるおいしさ最大の料理です。
y-2秒では、y-1秒で取った料理を除いたおいしさ最大の料理を取ります。
・・・これを繰り返し、y個の商品をgetします。

事前処理として、料理を無くなる時刻の早い順にソートしておきます。
これを最大値セグ木に載せます。

時刻sで取ることのできる商品の添え字を覚えておくことで、
1秒分の処理をO(logN)で実行可能です。

最大でN秒分の処理をする必要があるので、二分探索と合わせて
O(N*logN*logN) = O(4*10**7)ぐらいで処理できます。

t = [2,3,5,7,7,8]
ind_t = [0,0,1,2,2,3,3,5,6]

'''
