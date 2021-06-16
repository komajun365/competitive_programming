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

from math import gcd

n = int(input())
a = list(map(int,input().split()))

# primes = set()
# factors = []
# for ai in a:
#     res = factorization(ai)
#     factors.append(dict())
#     for p,cnt in res:
#         primes.add(p)
#         factors[-1][p] = cnt

# l = len(primes)
# encode = dict()
# for i,pi in enumerate(primes):
#     encode[pi] = i

# cnt = [[0] * l for _ in range(n)]
# for i in range(n):
#     for k,v in factors[i].items():
#         cnt[i][encode[k]] = v

rem = n
use = [0] * n
ans = []
while rem > 0:
    ng = True
    for i in range(n):
        if use[i] == 1:
            continue
        lcm = 1
        for j in range(n):
            if i == j or use[j] == 1:
                continue
            lcm = lcm * a[j] // gcd(lcm, a[j])
        # print(i,lcm)
        if lcm % a[i] != 0:
            ans.append(a[i])
            rem -= 1
            use[i] = 1
            ng = False
    
    if ng:
        print('No')
        exit()

ans = ans[::-1]
print('Yes')
print(' '.join(map(str,ans)))




#     max_num = [-1] * l
#     max_ind = [-1] * l
#     for i in range(n):
#         if use[i] == 1:
#             continue
#         for k,v in factors[i].items():
#             k = encode[k]
#             # print(k,v, max_num)
#             if max_num[k] < v:
#                 max_num[k] = v
#                 max_ind[k] = i
#             elif max_num[k] == v:
#                 max_ind[k] = -1
#         # print(i,a[i])
#         # print(max_num)
#         # print(max_ind)
    
#     cand = set()
#     for i in max_ind:
#         if i != -1:
#             cand.add(i)
    
#     if len(cand) == 0:
#         print('No')
#         exit()
    
#     for i in cand:
#         ans.append(a[i])
#         use[i] += 1
#         rem -= 1
    
#     # print(cand)
#     # print(max_num)
#     # print(max_ind)

# ans = ans[::-1]
# print('Yes')
# print(' '.join(map(str,ans)))


# # print(factors)
