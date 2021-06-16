# 行列関係
mod = 998244353

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

# 行列式 n*n行列 modは素数
def mat_det(x):
    n = len(x)
    if n == 1:
        return x[0][0]

    res = 1
    pm = 0
    for i in range(n-1):
        for j in range(i,n):
            if x[j][i] != 0:
                break
        else:
            return 0
        
        if i != j:
            x[i],x[j] = x[j],x[i]
            pm += 1
        inv = pow(x[i][i], mod-2, mod)
        res *= x[i][i]
        res %= mod
        for k in range(i,n):
            x[i][k] *= inv
            x[i][k] %= mod
        
        for j in range(i+1,n):
            mul = x[j][i]
            for k in range(i,n):
                x[j][k] -= x[i][k] * mul
                x[j][k] %= mod
    
    res *= x[-1][-1]
    if pm % 2 != 0:
        res *= -1
    res %= mod
    return res

        






