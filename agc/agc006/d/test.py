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

import itertools

# p = itertools.permutations(range(1,6))
# for i in p:
#     r3 = list(i)
#     r2 = [0] * 5
#     for i in range(3):
#         tmp = r3[i:i+3]
#         tmp.sort()
#         r2[i+1] = tmp[1]
#     r1 = [0]*5
#     tmp = r2[1:4]
#     tmp.sort()
#     r1[2] = tmp[1]
#     # print(r1)
#     print(r2)
#     # print(r3)
#     # print('')

n = 7
p = itertools.permutations(range(1,n+1))
r1s = set()
for i in p:
    r3 = list(i)
    r2 = [0] * n
    for i in range(n-2):
        tmp = r3[i:i+3]
        tmp.sort()
        r2[i+1] = tmp[1]
    # r2s.add(tuple(r2))
    r1 = [0] * n
    for i in range(n-4):
        tmp = r2[1+i:1+i+3]
        tmp.sort()
        r1[i+2] = tmp[1]
    r1s.add(tuple(r1))
r1s = list(r1s)
r1s.sort()
for i in r1s:
    print(i)


# for i in r2s:
#     print(i)
