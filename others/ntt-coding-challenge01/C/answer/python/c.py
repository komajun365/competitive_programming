#!/usr/bin/env python3

n, m = map(int,input().split())
l = list(map(int,input().split()))

def square(n):
    return n * n

d = {}
ans = 0
if n > 1:
    for i in range(n):
        for j in range(i):
            sum = square(l[i]) + square(l[j])
            diff = square(l[i]) - square(l[j])
            if diff < 0:
                diff *= -1
            if not (sum * 2) in d:
                d[sum * 2] = 0
            if not (diff * 2) in d:
                d[diff * 2] = 0
            d[sum * 2] += 1
            d[diff * 2] += 1

        s = square(l[i])
        if (s * 2) in d:
            ans += d[s * 2]

d2 = {}
if m > 1:
    for i in range(n):
        s = square(l[i])
        if not s in d2:
            d2[s] = 0
        d2[s] += 1

maxv = 0
for k, v in d.items():
    if k == 0:
        continue
    if k in d2:
        v2 = d2[k]
    else:
        v2 = 0

    sum = v * m + m * (m - 1) * v2 // 2

    maxv = max(maxv, sum)

for _, v in d2.items():
    sum = m * (m - 1) * v // 2

    maxv = max(maxv, sum)

print(ans + maxv)