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


import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

w,h = map(int,readline().split())
a = list(map(int,readline().split()))
b = list(map(int,readline().split()))
q = int(readline())
ab = list(map(int,read().split()))

def get_min_max(x):
    res = [[0,0] for _ in range(len(x))]
    res[0] = [x[0],x[0]]
    cumsum = x[::]
    for i in range(1,len(x)):
        cumsum[i] += cumsum[i-1]
    min_num = min(0,x[0])
    max_num = max(0,x[0])
    for i in range(1,len(x)):
        res[i][0] = min(res[i-1][0], cumsum[i] - max_num)
        res[i][1] = max(res[i-1][1], cumsum[i] - min_num)
        min_num = min(min_num,cumsum[i])
        max_num = max(max_num,cumsum[i])

    return res

a_min_max = get_min_max(a)
b_min_max = get_min_max(b)

ans = []
it = iter(ab)
for A,B in zip(it,it):
    A,B = A-1,B-1
    num = -1 * 10**11
    for i in a_min_max[A]:
        for j in b_min_max[B]:
            num = max(num,i*j)
    ans.append(num)

print(ans)
