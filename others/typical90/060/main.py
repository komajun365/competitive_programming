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

import bisect

n = int(input())
a = list(map(int,input().split()))

def calc_lis(x):
    lis = []
    res = [0] * n
    for i in range(n):
        num = bisect.bisect_left(lis, x[i])
        res[i] = num+1
        if len(lis) == num:
            lis.append(x[i])
        else:
            lis[num] = x[i]
    
    return res

res1 = calc_lis(a)
res2 = calc_lis(a[::-1])[::-1]

ans = 0
for i in range(n):
    ans = max(ans, res1[i] + res2[i] - 1)
print(ans)

# print(res1)
# print(res2)