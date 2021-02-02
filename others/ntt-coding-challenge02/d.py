# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

# defaultdict
from collections import defaultdict
# 二分木
import bisect

n,m = map(int,input().split())
a = list(map(int,input().split()))

cumsum = [0] * (n+1)
d = defaultdict(list)
cumsum_val = set()

for i in range(n):
    cumsum[i+1] = (cumsum[i] + a[i]) % m
    d[cumsum[i+1]].append(i+1)
    cumsum_val.add(cumsum[i+1])

cumsum_val = list(cumsum_val)
cumsum_val.sort()

ans = max(cumsum)
for i in range(1,n+1):
    ok = 0
    ng = n - cumsum[i] + 1
    for _ in range(50):
        mid = (ok+ng)//2
        while(True):
            ind = bisect.bisect_right(cumsum_val, mid) - 1
            
