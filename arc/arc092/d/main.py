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

# 解説ACです
# のはずがTLEが出たので定数倍に苦労しています。。。

from bisect import bisect_left

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

def next_sort(i,c):
    base1 = (1 << i) - 1
    cut = bisect_left(c, 1<<i)
    # c0 = c[:cut]
    c1 = [ci & base1 for ci in c[cut:]]
    l1 = n - cut
    i,j = 0,0
    res = []
    while i < cut or j < l1:
        if i == cut:
            res.append(c1[j])
            j += 1
        elif j == l1:
            res.append(c[i])
            i += 1
        else:
            if c[i] <= c1[j]:
                res.append(c[i])
                i += 1
            else:
                res.append(c1[j])
                j += 1
    return res

step1 = 14

ans = 0
c = b[:]
c.sort()
base = (1<<29) - 1
for i in range(28,step1,-1):
    bit = 1 << i
    bit2 = bit*2
    bit3 = bit*3
    cnt = 0
    for ai in a:
        ai &= base
        if ai <= bit:
            cnt += bisect_left(c, bit2-ai) - bisect_left(c, bit-ai)
        else:
            cnt += n - bisect_left(c, bit3-ai) + bisect_left(c, bit2-ai)
    ans += (cnt%2) << i
    if i == 0:
        break
    base >>= 1
    c = next_sort(i,c)
# print(ans)

c2 = [0] * (1<<(step1+1))
for ci in c:
    c2[ci] += 1

for i in range(step1,-1,-1):
    bit = 1 << i
    bit2 = bit*2
    bit3 = bit*3
    cs = [0] * (bit2+1)
    for j in range(bit2):
        cs[j] = cs[j-1] + c2[j]
    
    cnt = 0
    for ai in a:
        ai &= base
        if ai <= bit:
            cnt += cs[bit2-ai-1] - cs[bit-ai-1]
            # cnt += bisect_left(c, bit2-ai) - bisect_left(c, bit-ai)
        else:
            cnt += n - cs[bit3-ai-1] + cs[bit2-ai-1]
            # cnt += n - bisect_left(c, bit3-ai) + bisect_left(c, bit2-ai)
    ans += (cnt%2) << i
    if i == 0:
        break
    for j in range(bit):
        c2[j] += c2[j+bit]
    c2 = c2[:bit]
    base >>= 1

print(ans)



# ans = 0
# base = 0
# for i in range(29):
#     base = (base << 1) + 1
#     bit = 1 << i
#     c = [bi & base for bi in b]
#     c.sort()
#     cnt = 0
#     for ai in a:
#         ai &= base
#         if ai <= bit:
#             cnt += bisect_left(c, bit*2-ai) - bisect_left(c, bit-ai)
#         else:
#             cnt += n - bisect_left(c, bit*3-ai) + bisect_left(c, bit*2-ai)
#     ans += (cnt%2) << i
# print(ans)

