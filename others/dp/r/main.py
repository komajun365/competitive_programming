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

n,k,*a = map(int,read().split())
mod = 10**9+7

# 行列積
def mat_mul(x,y):
    xh = len(x)
    xw = len(x[0])
    yh = len(y)
    yw = len(y[0])
    assert xw == yh

    res = [[0] * yw for _ in range(xh)]
    for i in range(xh):
        for j in range(yw):
            for k in range(xw):
                res[i][j] += x[i][k] * y[k][j]
                res[i][j] %= mod
    return res


# 行列累乗
class matlix_power:
    def __init__(self, x, size):
        self.matrix = [x]
        self.n = len(x)
        self.size = size
        for i in range(size-1):
            self.matrix.append( mat_mul(self.matrix[-1], self.matrix[-1]) )
    
    def calc(self, k):
        res = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            res[i][i] = 1
        
        for i in range(self.size):
            if (k >> i)&1:
                res = mat_mul(self.matrix[i], res)
        return res

mat = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        mat[i][j] = a[i*n+j]

mp = matlix_power(mat, 60)
res = mp.calc(k)

ans = 0
for i in range(n):
    ans += sum(res[i])
    ans %= mod
print(ans)