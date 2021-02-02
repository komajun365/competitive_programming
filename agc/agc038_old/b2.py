# import numpy as np

n,k = map(int, input().split())
p_list = tuple(map(int, input().split()))

p_before = 200001
up = 0

mins = [0]*(n+1-k)
maxs = [0]*(n+1-k)

for i in range(n+1-k):
    temp = p_list[i:i+k]
    mins[i] = min(temp)
    maxs[i] = max(temp)

mins = mins[:-1]
maxs = maxs[1:]

origin = 0
not_origin = 0

for p in p_list[:k]:
    if p_before < p:
        up += 1
    else:
        up=0
    p_before = p*1

    if p == p_list[k-1]:
        if up >= k-1:
            origin = 1
        else:
            not_origin = 1


for p,i in zip(p_list[k:], range(k,n)):
    if p_before < p:
        up += 1
    else:
        up=0
    p_before = p*1

    if up >= k-1:
        origin = 1
    else:
        if p_list[i-k] == mins[i-k]:
            if p_list[i] != maxs[i-k]:
                not_origin += 1
        else:
            not_origin += 1


print(origin + not_origin)
