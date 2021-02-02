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

from heapq import heappop,heappush

k = int(input())

def calc_sn(x):
    res = 0
    while(x > 0):
        res += x%10
        x //= 10
    return res

x = 10**15-1
min_n = x
min_sn = 9*15
nums = []
done = set()
hq = [-x]
while(hq):
    i = heappop(hq) * -1
    sn_i = calc_sn(i)
    if min_n * sn_i >= i * min_sn:
        nums.append(i)
        min_n = i
        min_sn = sn_i
    else:
        continue
    x = i
    ex = 1
    for j in range(16):
        if(ex >= i):
            break
        cand = i - ex
        ex *= 10
        if cand in done:
            continue
        sn_c = calc_sn(i)
        if min_n * sn_c >= cand * min_sn:
            done.add(cand)
            heappush(hq, -cand)

ans = nums[::-1]
print('\n'.join(map(str,ans[:k])))

print(len(ans))






# n = 10**6
# sn = [0] * n
# for i in range(1,n):
#     s = 0
#     x = i
#     while(x > 0):
#         s += x%10
#         x //= 10
#     sn[i] = i / s

# min_n = n
# for i in range(n-1,0,-1):
#     if(sn[i] < min_n):
#         print(i,sn[i])
#         min_n = sn[i]

