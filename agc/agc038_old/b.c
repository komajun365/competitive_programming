import heapq

n,k = map(int, input().split())
p_list = list(map(int, input().split()))

p_before = 200001
up = 0

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
        if p_list[i-k] == min(p_list[(i-k):i]):
            if p_list[i] != max(p_list[(i-k+1):(i+1)]):
                not_origin += 1
        else:
            not_origin += 1


print(origin + not_origin)
