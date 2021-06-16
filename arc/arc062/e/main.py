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
# from collections import defaultdict

n,*c = map(int,read().split())

# def rotate(x):
#     res = x[:]
#     for _ in range(3):
#         x = x[1:] + x[:1]
#         if res > x:
#             res = x[:]
#     return res

def get_num(x):
    var = 1
    res = []
    if x[0] == x[1] == x[2] == x[3]:
        var = 4
        res.append((x[0] << 30) | (x[1] << 20) | (x[2] << 10) | x[3])
    elif x[0] == x[2] and x[1] == x[3]:
        var = 2
        res.append((x[0] << 30) | (x[1] << 20) | (x[2] << 10) | x[3])
        res.append((x[1] << 30) | (x[2] << 20) | (x[3] << 10) | x[0])
    else:
        res.append((x[0] << 30) | (x[1] << 20) | (x[2] << 10) | x[3])
        res.append((x[1] << 30) | (x[2] << 20) | (x[3] << 10) | x[0])
        res.append((x[2] << 30) | (x[3] << 20) | (x[0] << 10) | x[1])
        res.append((x[3] << 30) | (x[0] << 20) | (x[1] << 10) | x[2])

    return var, min(res)

d = dict()
nums = []
tiles = []

it = iter(c)
for i,*x in zip(range(n), it,it,it,it):
    tiles.append(list(x))
    _,num = get_num(x)
    nums.append(num)
    if num in d:
        d[num] += 1
    else:
        d[num] = 1 
    

ans = 0
for i in range(n-5):
    x = tiles[i]
    d[nums[i]] -= 1
    for j in range(i+1,n):
        y = tiles[j][:]
        d[nums[j]] -= 1
        for _ in range(4):
            y = y[1:] + y[:1]
            comb = 1
            z0 = [x[0],y[1],y[0],x[1]]
            v0,n0 = get_num(z0)
            if not n0 in d:
                continue 
            comb *= v0 * d[n0]
            
            z1 = [x[1],y[0],y[3],x[2]]
            v1,n1 = get_num(z1)
            if not n1 in d:
                continue 
            dup = 1 * (n0 == n1)
            comb *= v1 * (d[n1] - dup)

            z2 = [x[2],y[3],y[2],x[3]]
            v2,n2 = get_num(z2)
            if not n2 in d:
                continue 
            dup = 1 * (n0 == n2) + 1 * (n1 == n2)
            comb *= v2 * (d[n2] - dup)

            z3 = [x[3],y[2],y[1],x[0]]
            v3,n3 = get_num(z3)
            if not n3 in d:
                continue 
            dup = 1 * (n0 == n3) + 1 * (n1 == n3) + 1 * (n2 == n3)
            comb *= v3 * (d[n3] - dup)
            ans += comb

        d[nums[j]] += 1

print(ans)

    

