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

# 前処理
b_len = min(10, n.bit_length()-1)
max_bef = 2**b_len

bef = [ [] for _ in range(2**b_len)]
bef[1] = [(0,0),(W[0],V[0])]

for i in range(2,max_bef):
    iw,iv = W[i-1],V[i-1]
    j = i//2
    while(j > 0):
        for jw,jv in bef[j]:
            bef[i].append((iw+jw,iv+jv))
        j //= 2

bef_max = [ [0]*(10**5 + 1) for _ in range(max_bef)]

for i in range(1,max_bef):
    j = i
    while(j > 0):
        for jw,jv in bef[j]:
            bef_max[i][jw] = max(bef_max[i][jw], jv)
        j //= 2

    for j in range(1,10**5+1):
        bef_max[i][j] = max(bef_max[i][j],bef_max[i][j-1])

for i in bef_max:
    print(i[100:150])

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

    aft = [(0,0)]
    x = vi
    max_ans = bef_max[par][Li]
    while(x >= max_bef):
        xw,xv = W[x-1],V[x-1]
        aft2 = []
        for jw,jv in aft:
            jw += xw
            jv += xv
            lim_w = Li - jw
            if(lim_w < 0):
                continue
            aft2.append((jw,jv))
            max_ans = max(max_ans, bef_max[par][lim_w]+jv)
        x //= 2
        aft = aft + aft2

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
