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

n = int(readline())
data = list(map(int,read().split()))

V = data[:2*n:2]
W = data[1:2*n:2]
q = data[2*n]
v = data[2*n+1::2]
L = data[2*n+2::2]

if(n==1):
    ans = []
    for i,j in zip(v,L):
        if(W[i-1] <= j):
            ans.append(V[0])
        else:
            ans.append(0)
    print('\n'.join(map(str,ans)))
    exit()

def merge(before, xw,xv):
    after = [[0,0] for _ in range(len(before))]
    for i,(w,v) in enumerate(after):
        after[i][0] = xw + before[i][0]
        after[i][1] = xv + before[i][1]

    res = []
    i = 0
    j = 0
    while(i < len(before)):
        if(before[i][0] <= after[j][0]):
            res.append(before[i][::])
            i += 1
        else:
            res.append(after[j][::])
            j += 1

    while(j < len(before)):
        res.append(after[j][::])
        j += 1

    return res


# 前処理　最大2**10まで前計算
b_len = min(10, n.bit_length()-1)
n_bef = 2**b_len
bef = [[] for _ in range(n_bef)]
bef[1] = [[0,0],[W[0],V[0]]]
for i in range(2,n_bef):
    bef[i] = merge(bef[i//2], W[i-1], V[i-1])


ans = []
for vi,Li in zip(v,L):
    if(vi==1):
        if(W[0] <= Li):
            ans.append(V[0])
        else:
            ans.append(0)
        continue

    par = vi
    aft = [[0,0]]
    while(par >= n_bef):
        aft = merge(aft, W[par-1], V[par-1])
        par //= 2

    max_ans = 0
    max_bef_v = 0
    i_bef = 0
    for aw,av in aft[::-1]:
        lim_w = Li - aw
        if(lim_w < 0):
            continue

        while(i_bef < len(bef[par])):
            if(bef[par][i_bef][0] > lim_w):
                break
            max_bef_v = max(max_bef_v,bef[par][i_bef][1])
            i_bef += 1
        max_ans = max(max_ans, av + max_bef_v)

    ans.append(max_ans)

print('\n'.join(map(str,ans)))



# print(n)
# print(V)
# print(W)
# print(q)
# print(v)
# print(L)

'''


'''
