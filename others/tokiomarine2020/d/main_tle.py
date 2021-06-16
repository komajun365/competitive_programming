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

import sys
read = sys.stdin.buffer.read

n,*data = map(int,read().split())
VW = data[:2*n]
q = data[2*n]
vL = data[2*n+1:]

d = n.bit_length()
d2 = d//2

half = [[] for _ in range(2**d2)]
half[0].append([0,0])

for i in range(1,2**d2):
    V,W = VW[(i-1)*2:i*2]
    for vj,wj in half[i//2]:
        half[i].append([vj,wj])
        if W + wj <= 100000:
            half[i].append([vj+V,wj+W])
    half[i].sort(key = lambda x: x[1])

def make_vw(x,L):
    l = len(x)
    res = [[0,0]]
    for i in range(l):
        l2 = len(res)
        vi,wi = x[i]
        res2 = []
        for j in range(l2):
            vj,wj = res[j]
            if wi + wj <= L:
                res2.append([vi+vj,wi+wj])
        res3 = []
        j,k = 0,0
        while j < len(res) or k < len(res2):
            if j == len(res):
                res3.append(res2[k][:])
                k += 1
            elif k == len(res2):
                res3.append(res[j][:])
                j += 1
            else:
                if res[j][1] > res2[k][1]:
                    res3.append(res[j][:])
                    j += 1
                else:
                    res3.append(res2[k][:])
                    k += 1
                
        res,res3 = res3,res

    return res

def excute_query(v,L):
    dv = v.bit_length()
    res = 0
    if dv <= d2:
        for vi,wi in half[v]:
            if wi <= L:
                res = max(res,vi)
        return res
    
    x = []
    i = v
    while i >= 2**d2:
        V,W = VW[(i-1)*2:i*2]
        x.append([V,W])
        i //= 2
    upper = half[i]
    under = make_vw(x,L)
    j = 0
    upper_max = 0
    for vk,wk in under:
        while j < len(upper):
            vj,wj = upper[j]
            if wj + wk <= L:
                upper_max = max(upper_max, vj)
                j += 1
            else:
                break
        res = max(res, vk + upper_max)
    # print(v,L,res)
    # print(upper)
    # print(under)
    return res

ans = []
it = iter(vL)
for v,L in zip(it,it):
    ans.append(excute_query(v,L))

print('\n'.join(map(str,ans)))














