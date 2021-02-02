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

p = 10**8
a = 1777
n = 1855
# a,n = 3,3

ex = 1
for i in range(n):
    ex %= (p-1)
    ex = pow(a,ex,p)

print(ex)


'''
寿司　虚空編！

1777↑↑1 = 1777
1777↑↑2 = 1777^1777
1777↑↑3 = 1777^(1777^1777)
1777↑↑4 = 1777^(1777^(1777^1777))

最後の８桁なので
mod 10**8がわかればよいってやつ

どこでループするのか？

フェルマーの小定理。
1777と10**8は素なので、
1777 = 1777^(10**8)
1 = 1777^(10**8-1)

'''
