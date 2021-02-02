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

V = tuple(data[:2*n:2])
W = tuple(data[1:2*n:2])
q = data[2*n]
v = tuple(data[2*n+1::2])
L = tuple(data[2*n+2::2])

if(n==1):
    ans = []
    for i,j in zip(v,L):
        if(W[i-1] <= j):
            ans.append(V[0])
        else:
            ans.append(0)
    print('\n'.join(map(str,ans)))
    exit()

# 前処理　最大2**9まで前計算
b_len = min(9, n.bit_length()-1)
max_bef = 2**b_len
bef = [ [0]*(10**5 + 1) for _ in range(max_bef)]

for i in range(1,max_bef):
    iw,iv = W[i-1],V[i-1]
    par = i//2
    for j in range(1,10**5+1):
        if(j>=iw):
            bef[i][j] = max(bef[par][j] , bef[par][j-iw]+iv)
        else:
            bef[i][j] = bef[par][j]

ans = []
for vi,Li in zip(v,L):
    if(vi==1):
        if(W[0] <= Li):
            ans.append(V[0])
        else:
            ans.append(0)
        continue

    par = vi
    while(par>= max_bef):
        par //= 2

    max_ans = bef[par][Li]
    aft = [(0,0)]
    x = vi
    while(x >= max_bef):
        xw,xv = W[x-1],V[x-1]
        x //= 2
        if(x < max_bef):
            lim_j = len(aft)
            for j in range(lim_j):
                jw,jv = aft[j]
                jw += xw
                jv += xv
                lim_w = Li - (jw)
                if(lim_w >= 0):
                    max_ans = max(max_ans, bef[par][lim_w]+jv)
            break


        lim_j = len(aft)
        for j in range(lim_j):
            jw,jv = aft[j]
            jw += xw
            jv += xv
            lim_w = Li - (jw)
            if(lim_w >= 0):
                max_ans = max(max_ans, bef[par][lim_w]+jv)
                aft.append((jw,jv))

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
