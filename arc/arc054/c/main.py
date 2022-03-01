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

n = int(input())
mat = []
for _ in range(n):
    mat.append([])
    for si in input():
        mat[-1].append(int(si))

mod = 2
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

ans = mat_det(mat)
if ans == 0:
    print('Even')
else:
    print('Odd')