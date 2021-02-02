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

'''
10C6 = 210

210**2 * 20 余裕。

'''

import itertools

def check(ai,bi,num1,num2):
    if(len(ai)!=6):
        ai = list(ai)
        ai = ai + [6]
    if(len(bi)!=6):
        bi = list(bi)
        bi = bi + [6]

    res = 0
    res += ((num1 in ai) + (num2 in bi))//2
    res += ((num2 in ai) + (num1 in bi))//2
    return res > 0

ans = 0
base = [0,1,2,3,4,5,7,8]
a1 = itertools.combinations(base, 6)
a2 = itertools.combinations(base, 5)
a3 = itertools.combinations(base, 4)
for a in [a1,a2,a3]:
    for ai in a:

        b1 = itertools.combinations(base, 6)
        b2 = itertools.combinations(base, 5)
        b3 = itertools.combinations(base, 4)
        for b in [b1,b2,b3]:
            for bi in b:
                # check
                for num1,num2 in zip([0,0,0,1,2,3,4,6,8],[1,4,6,6,5,6,6,4,1]):
                    if(not check(ai,bi,num1,num2)):
                        break
                else:
                    ans += 1

print(ans)




# base = [0,1,2,3,4,5,6,6,7,8]
# a = itertools.combinations(base, 6)
#
# def check(ai,bi,num1,num2):
#     res = 0
#     res += ((num1 in ai) + (num2 in bi))//2
#     res += ((num2 in ai) + (num1 in bi))//2
#     return res > 0
#
# ans = 0
# for ai in a:
#     b = itertools.combinations(base, 6)
#     for bi in b:
#         # check
#         for num1,num2 in zip([0,0,0,1,2,3,4,6,8],[1,4,6,6,5,6,6,4,1]):
#             if(not check(ai,bi,num1,num2)):
#                 break
#         else:
#             pl = 4
#             if(ai.count(6)==1):
#                 pl = pl//2
#             if(bi.count(6)==1):
#                 pl = pl//2
#             ans += pl
#
# print(ans//4)

# for ai in a:
#     b = itertools.combinations(base, 6)
#     for bi in b:
#         # check
#         for num1,num2 in zip([1,2,3,4,5,6],[1,2,3,4,5,6]):
#             if(not check(ai,bi,num1,num2)):
#                 break
#         else:
#             ans += 1
#
# print(ans)


# a = itertools.combinations([1,2,3], 2)
# b = itertools.combinations([4,5,6], 2)
# for i in [a,b]:
#     for j in i:
#         print(j)
