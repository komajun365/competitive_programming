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

def floor_sum(n, m, a, b):
    """
    Σ^{n-1}_{0} ((a*i+b)//m)を計算する。

    Parameters
    ----------
    n : int
    m : int
    a : int
    b : int
        0 <= n
        1 <= m
        0 <= a,b < m

    Returns
    -------
    ans : int
    """
    ans = 0
    while True:
        if a >= m:
            ans += (n - 1) * n * (a // m) // 2
            a %= m
        if b >= m:
            ans += n * (b // m)
            b %= m

        y_max = (a * n + b) // m
        x_max = y_max * m - b
        if y_max == 0:
            return ans
        ans += (n - (x_max + a - 1) // a) * y_max
        n, m, a, b = y_max, a, m, (a - x_max % a) % a


import sys
read = sys.stdin.buffer.read

t,*case = map(int,read().split())

def solve(n,ax,bx,ay,by):
    if ax > ay:
        ax,ay = ay,ax
        bx,by = by,bx
    d = ay - ax
    if d != 0 and by <= bx:
        return 0
    if bx == by:
        if d == 0:
            return n
        else:
            return 0
    if d == 0 and by < bx:
        ax,ay = ay,ax
        bx,by = by,bx
    
    # # -1 ~ 0
    # if d != 0:
    #     left = -( -bx*by*(d-1) // (by-bx))
    #     right = bx*by*d // (by-bx)

    l1 = bx*by*(d-1) // (by-bx) + 1
    r1 = bx*by*d // (by-bx)
    l2 = bx*by*d // (by-bx) + 1
    r2 = bx*by*(d+1) // (by-bx)
    
    l1 = max(1, l1)
    r1 = min(n,r1)
    l2 = max(1,l2)
    r2 = min(n,r2)
    res = max(0, r2 - l1 + 1)
    # print(n,ax,bx,ay,by)
    # print(l1,r1,l2,r2)
    for l,r in [[l1,r1],[l2,r2]]:
        if l > r:
            continue

        tot1 = floor_sum(r+1, bx, 1, 0) - floor_sum(l, bx, 1, 0)
        tot2 = floor_sum(r+1, by, 1, 0) - floor_sum(l, by, 1, 0) + (r-l+1) * d
        res -= abs(tot1 - tot2)
        # print(l,r,tot1,tot2)
    return res

ans = []
it = iter(case)
for n,ax,bx,ay,by in zip(it,it,it,it,it):
    ans.append(solve(n,ax,bx,ay,by))
print('\n'.join(map(str,ans)))



'''
n/bx + 1 = d + n/by
n * (1/bx - 1/by) = (d-1)
n * (by - bx)/bx*by = (d-1)
n = bx*by*(d-1)/(by-bx)



'''


        