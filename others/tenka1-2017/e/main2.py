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


import sys
read = sys.stdin.buffer.read
from operator import itemgetter

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
        return self._sum(r) - self._sum(l)


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
        

def calc(abc):
    degs = []
    for i in range(n):
        a,b,c = abc[i]
        degs.append([-a/b,i])
    degs.sort()
    deg_idx = [-1] * n
    for i in range(n):
        _, idx = degs[i]
        deg_idx[idx] = i
    
    ok = -1
    ng = 1
    if not check(-1, abc, degs, deg_idx):
        ok = -2 * 10**8
        ng = -1
    elif check(1, abc, degs, deg_idx):
        ok = 1
        ng = 2 * 10**8
    
    if ok == -1:
        for _ in range(60):
            mid = (ok+ng)/2
            if mid == ok or mid == ng:
                break
            if check(mid, abc, degs, deg_idx):
                ok = mid
            else:
                ng = mid
            dif = ng-ok
            if dif < 10**-9:
                break
    else:
        for _ in range(60):
            mid = (ok*ng)**0.5
            if ok < 0:
                mid *= -1
            if check(mid, abc, degs, deg_idx):
                ok = mid
            else:
                ng = mid
            dif = ng-ok
            if dif/min(abs(ok),abs(ng)) < 10**-9:
                break
            # print(_,ok,ng)
   
    return ok

under = (n*(n-1)//2 - 1)//2
ans_x = calc(abc)

abc_y = []
for a,b,c in abc:
    abc_y.append([-b/a, 1, -c/a])

ans_y = calc(abc_y)

print(ans_x, ans_y)

