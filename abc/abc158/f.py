import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
input = sys.stdin.readline

n = int(input())
xd = [list(map(int, input().split())) for _ in range(n)]

mod = 998244353

xd.sort()

# 最大値を求めるセグメント木

def init_max(init_max_val):
    #set_val
    for i in range(n):
        seg_max[i+num_max-1]=init_max_val[i]
    #built
    for i in range(num_max-2,-1,-1) :
        seg_max[i]=max(seg_max[2*i+1],seg_max[2*i+2])

def update_max(k,x):
    k += num_max-1
    seg_max[k] = x
    while k:
        k = (k-1)//2
        seg_max[k] = max(seg_max[k*2+1],seg_max[k*2+2])

def query_max(p,q):
    if q<=p:
        return ide_ele_max
    p += num_max-1
    q += num_max-2
    res=ide_ele_max
    while q-p>1:
        if p&1 == 0:
            res = max(res,seg_max[p])
        if q&1 == 1:
            res = max(res,seg_max[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = max(res,seg_max[p])
    else:
        res = max(max(res,seg_max[p]),seg_max[q])
    return res

#####単位元######
ide_ele_max = -1

#num_max:n以上の最小の2のべき乗
# num_max =2**(n-1).bit_length()
num_max = 2**(len(str(bin(n-1))) -2)
seg_max=[ide_ele_max]*2*num_max

import bisect
xs = list(map(lambda x: x[0], xd))

ans = [0]*(n+1)
ans[-1] = 1

for i in range(n-1, -1, -1):
    move_r = bisect.bisect_left(xs, sum(xd[i]))
    if(i+1 == move_r):
        update_max(i, i)
    else:
        update_max(i, query_max(i+1, move_r))

    ans[i] = (ans[i+1] + ans[seg_max[i + num_max - 1] + 1]) % mod

print(ans[0])
