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

s = int(input())
mod = 998244353

s -= 6

def matmul(x,y):
    size = len(x)
    res = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                res[i][j] += x[i][k] * y[k][j]
            res[i][j] %= mod
    return res

def solve(nums):
    mat = [[0] * 6 for _ in range(6)]
    for i in range(5):
        mat[i+1][i] = 1
    l = len(nums)
    for i in range(1,2**l):
        x = -1
        flags = 0
        for j in range(l):
            if (i >> j) & 1:
                flags += 1
                x += nums[j]
        if flags % 2 == 0:
            mat[0][x] -= 1
        else:
            mat[0][x] += 1            
    
    mat_ex = [mat]
    for _ in range(60):
        mat_ex.append( matmul(mat_ex[-1], mat_ex[-1]) )
    
    res = [[0] * 6 for _ in range(6)]
    for i in range(6):
        res[i][i] = 1

    for i in range(61):
        if (s >> i) & 1:
            res = matmul(mat_ex[i], res)
    
    return res[0][0]

c111111 = solve([1,1,1,1,1,1])
# c21111 = solve([2,1,1,1,1])
# c3111 = solve([3,1,1,1])
c2211 = solve([2,2,1,1])
c411 = solve([4,1,1])
# c321 = solve([3,2,1])
c222 = solve([2,2,2])
# c51 = solve([5,1])
# c42 = solve([4,2])
c33 = solve([3,3])
# c6 = solve([6])

ans = 0
ans += c111111 * 1
ans += c2211 * 3
ans += c411 * 6
ans += c222 * 6
ans += c33 * 8

ans %= mod
ans *= pow(24,mod-2,mod)
ans %= mod
print(ans)

# print(c111111)
# print(c2211)
# print(c411,c222)
# print(c33)