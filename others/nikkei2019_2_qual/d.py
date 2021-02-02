# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
input = sys.stdin.readline

n,m = map(int,input().split())

# 最小値を求めるセグメント木
def init_min(init_min_val):
    #set_val
    for i in range(n):
        seg_min[i+num_max-1]=init_min_val[i]
    #built
    for i in range(num_max-2,-1,-1) :
        seg_min[i]=min(seg_min[2*i+1],seg_min[2*i+2])

def update_min(k,x):
    k += num_max-1
    seg_min[k] = x
    while k:
        k = (k-1)//2
        seg_min[k] = min(seg_min[k*2+1],seg_min[k*2+2])

def query_min(p,q):
    if q<=p:
        return ide_ele_min
    p += num_max-1
    q += num_max-2
    res=ide_ele_min
    while q-p>1:
        if p&1 == 0:
            res = min(res,seg_min[p])
        if q&1 == 1:
            res = min(res,seg_min[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = min(res,seg_min[p])
    else:
        res = min(min(res,seg_min[p]),seg_min[q])
    return res

#####単位元######
ide_ele_min = 10**20

#num_max:n以上の最小の2のべき乗
# num_max =2**(n-1).bit_length()
num_max = 2**(len(str(bin(n-1))) -2)
seg_min=[ide_ele_min]*2*num_max

update_min(0,0)

rlc = []
for i in range(m):
    l,r,c = map(int,input().split())
    rlc.append((r,l,c))

rlc.sort()

for tmp in rlc:
    r,l,c = tmp
    l = l-1
    r = r-1
    update_min( r, min( query_min(l,r) + c , query_min(r,r+1)) )

ans = query_min(n-1,n)
if(ans == ide_ele_min):
    print(-1)
else:
    print(ans)
