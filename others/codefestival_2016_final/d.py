# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,m = map(int,input().split())
x = list(map(int,input().split()))

import collections
c = collections.Counter(x)

rems = [[0] * 2 for _ in range(m)]

for key, val in c.items():
    rems[key%m][0] += val%2
    rems[key%m][1] += (val//2) * 2

ans = 0
for i in range(1 + m//2):
    if(i*2 == m)|(i==0):
        ans += sum(rems[i])//2
        continue

    j = m-i
    if(sum(rems[i]) < sum(rems[j])):
        pair_mul = sum(rems[i])
        more = j
    else:
        pair_mul = sum(rems[j])
        more = i
    pair_same = (rems[more][1] - max(pair_mul - rems[more][0], 0))//2
    ans += pair_mul + pair_same

print(ans)
