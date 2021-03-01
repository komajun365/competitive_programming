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

# a = input()
# b = input()
# c = input()

def calc(a,b,c)
    abc = [a,b,c]

    base = ord('a')
    abc2 = [[],[],[]]
    for i in range(3):
        for si in abc[i]:
            if si =='?':
                abc2[i].append(-1)
            else:
                abc2[i].append( ord(si) - base)

    match = []
    for i in range(3):
        match.append([[] for _ in range(3)])
        for j in range(3):
            if i == j:
                continue
            li = len(abc2[i])
            lj = len(abc2[j])
            match[i][j] = [0] * (li+1)
            match[i][j][-1] = 1
            for i_idx in range(li):
                for j_idx in range(lj):
                    if i_idx + j_idx == li:
                        match[i][j][i_idx] = 1
                        break
                    if abc2[i][i_idx + j_idx] != abc2[j][j_idx] and \
                    abc2[i][i_idx + j_idx] != -1 and \
                    abc2[j][j_idx] != -1:
                        break               
                else:
                    match[i][j][i_idx] = 1

    ans = 6000
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            k = 3-i-j
            for i_idx in range(len(abc2[i]) + 1):
                for j_idx in range(len(abc2[j]) + 1):
                    if match[i][j][min(i_idx, len(abc2[i]))] == 1 and \
                    match[i][k][min(i_idx+j_idx, len(abc2[i]))] == 1 and \
                    match[j][k][min(j_idx, len(abc2[j]))] == 1:
                        tmp = max(len(abc2[i]), i_idx + len(abc2[j]), i_idx+j_idx+len(abc2[k]))
                        ans = min(ans, tmp)

    # print(ans)
    return ans


# def calc_test(a,b,c):
#     la = len(a)
#     lb = len(b)
#     lc = len(c)
#     res = la+lb+lc
#     abc = [a,b,c]
#     for i in range(3):
#         for j in range(3):
#             if i==j:
#                 continue
#             k = 3-i-j
#             li = len(abc[i])
#             lj = len(abc[j])
#             lk = len(abc[k])
#             for ii in range(li+1):
#                 s = abc[i][::]
#                 for ji in range(lj):
#                     if abc[i][ii+ji] != abc[j][ji] and


        


# for i in range(3):
#     for j in range(3):
#         print(match[i][j])

part = ['abcdefghijklmnopqrstuvwxyz???']
pl = len(part)

from random import randint
for _ in range(30):
    la = randint(5,10)
    lb = randint(5,10)
    lc = randint(5,10)
    for i in range(la):
        a += part[ randint(0,pl-1)]
    for i in range(lb):
        b += part[ randint(0,pl-1)]
    for i in range(lc):
        c += part[ randint(0,pl-1)]
    
    ans1 = calc(a,b,c)



