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

# 前処理　最大2**10まで前計算
b_len = min(10, n.bit_length()-1)

bef = [ [] for _ in range(2**b_len)]
bef[1] = [(0,0),(W[0],V[0])]

for i in range(2,2**b_len):
    iw,iv = W[i-1],V[i-1]
    bef[i] = bef[i//2][::]
    for jw,jv in bef[i//2]:
        bef[i].append((iw+jw,iv+jv))

for i in range(1,2**b_len):
    bef[i].sort()

#
# print(bef)
# print(len(bef))
# print(b_len,2**b_len)

ans = []
for vi,Li in zip(v,L):
    if(vi==1):
        if(W[0] <= Li):
            ans.append(V[0])
        else:
            ans.append(0)
        continue

    aft = [(0,0)]
    x = vi
    while(x >= 2**b_len):
        xw,xv = W[x-1],V[x-1]
        aft2 = aft[::]
        for jw,jv in aft:
            aft2.append((xw+jw,xv+jv))
        x //= 2
        aft = aft2[::]

    aft.sort(reverse=True)

    max_ans = 0
    max_bef_v = 0
    i_bef = 0
    for aw,av in aft:
        lim_w = Li - aw
        if(lim_w < 0):
            continue

        while(i_bef < len(bef)):
            if(bef[x][i_bef][0] > lim_w):
                break
            max_bef_v = max(max_bef_v,bef[x][i_bef][1])
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
