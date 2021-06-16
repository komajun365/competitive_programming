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

k,m = map(int,input().split())
a = list(map(int,input().split()))
c = list(map(int,input().split()))

base = (1<<32) - 1
def matmul(a,b):
    res = [[0] * k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            for l in range(k):
                res[i][j] ^= a[i][l] & b[l][j]
    return res

def calc(x):
    mat = [[0] * k for _ in range(k)]
    for i in range(k-1):
        mat[i][i+1] = base
    for i in range(k):
        mat[-1][i] = c[k-i-1]
    
    ex = [mat]
    for _ in range(32):
        ex.append(matmul(ex[-1], ex[-1]))
    
    mat_x = [[0] * k for _ in range(k)]
    for i in range(k):
        mat_x[i][i] = base
    
    for i in range(32):
        if (x >> i) & 1:
            mat_x = matmul(ex[i], mat_x)
    
    res = 0
    for i in range(k):
        res ^= a[i] & mat_x[0][i]
    return res

print(calc(m-1))
    

    
    


