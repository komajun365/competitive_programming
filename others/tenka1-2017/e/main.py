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

"""
怪しい枝刈りで通したのでメモを残しておきます。
普通にやるとx軸、y軸ごとに二分探索を60回程度やる必要があります。
が、これだとTLEします。
（雑な計測ですが、私のコードだと50回ぐらいでTLEになりそうです。）

なので、二分探索する範囲を減らしたいです。
交点のx,y座標は最悪abs(2*10**8)くらいになると思われるのですが、
Nが大きいケースでの出力解はもっと原点に近かったり、
あるいは交点が出現する範囲はもっと狭いのではないかと推測します。

そこで交点を乱択します。
このコードでは1000個程度の交点座標を計算し、
その中で上から20番目と下から20番目の点を
二分探索の探索上下限にしました。

すると良い感じに計算量が減ったらしく、ぎりぎり通るようになっています。
（たぶん4600~4700msecぐらいで通っているはずです。）

＃　もしこれを読んでいる方で、
　　このコードの計算量改善点があれば教えていただけると大変喜びます。
"""


import sys
read = sys.stdin.buffer.read
from operator import itemgetter
import random

class FenwickTree:
    def __init__(self, n: int):
        self.__n = n
        self.__data = [0] * self.__n

    def add(self, p: int, x: int):
        # assert (0 <= p) & (p < self.__n)
        p += 1
        while(p <= self.__n):
            self.__data[p - 1] += x
            p += p & -p

    def sum(self, l: int, r: int):
        # assert (0 <= l) & (l <= r) & (r <= self.__n)
        return self.__sum(r) - self.__sum(l)


    def _sum(self, r: int):
        s = 0
        while(r > 0):
            s += self.__data[r - 1]
            r -= r & -r
        return s

n,*data = map(int,read().split())

abc = []
it = iter(data)
for a,b,c in zip(it,it,it):
    abc.append([a,b,c])

# 交点乱択
xs = []
ys = []
for _ in range(1000):
    i = random.randint(0,n-1)
    j = (random.randint(1,n-1) + i) % n
    ai,bi,ci = abc[i]
    aj,bj,cj = abc[j]
    x = (bi*cj-ci*bj)/(aj*bi-ai*bj)
    y = (ai*cj-ci*aj)/(bj*ai-bi*aj)
    xs.append(x)
    ys.append(y)

xs.sort()
ys.sort()



def check(x, abc, degs, deg_idx):
    ys = []
    for i in range(n):
        a,b,c = abc[i]
        y = (-a*x+c)/b
        ys.append([y,i])
    ys.sort(key=itemgetter(0))
    
    ft = FenwickTree(n)

    left = 0
    for i in range(n):
        idx = deg_idx[ys[i][1]]
        left += ft._sum(idx)
        ft.add(idx,1)
    
    # print(x,left,under)
       
    if left <= under:
        return True
    else:
        return False
        

def calc(abc, upper , downer):
    degs = []
    for i in range(n):
        a,b,c = abc[i]
        degs.append([-a/b,i])
    degs.sort()
    deg_idx = [-1] * n
    for i in range(n):
        _, idx = degs[i]
        deg_idx[idx] = i
    
    
    ok = downer
    ng = upper
    for _ in range(60):
        mid = (ok+ng)/2
        if mid == ok or mid == ng:
            break
        if check(mid, abc, degs, deg_idx):
            ok = mid
        else:
            ng = mid
        dif = ng-ok
        if dif * 10**9 < min(abs(ok),abs(ng)) or dif < 10**-9:
            # print(_)
            break

    return ok

under = (n*(n-1)//2 - 1)//2
ans_x = calc(abc, xs[-20], xs[20])

abc_y = []
for a,b,c in abc:
    abc_y.append([-b/a, 1, -c/a])

ans_y = calc(abc_y, ys[-20], ys[20])

print(ans_x, ans_y)

