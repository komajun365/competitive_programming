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
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

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
    while(True):
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

t,*nmab = map(int,read().split())

ans = []
it = iter(nmab)
for n,m,a,b in zip(it,it,it,it):
    ans.append(floor_sum(n,m,a,b))
print('\n'.join(map(str,ans)))
# print(*ans, sep='\n')
