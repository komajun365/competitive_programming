import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
h = list(map(int, input().split()))
a = list(map(int, input().split()))

# セグメント木を使うといいらしい

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
ide_ele_max = 0

#num_max:n以上の最小の2のべき乗
# num_max =2**(n-1).bit_length()
num_max = 2**(len(str(bin(n-1))) -2)
seg_max=[ide_ele_max]*2*num_max

for i in range(n):
    h_i = h[i]
    update_max( h_i-1, query_max(0,h_i) + a[i] )

print(query_max(0,n))
