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

from collections import defaultdict

n,m = map(int,input().split())
a = list(map(int,input().split()))

cumsum = [[0,0] for _ in range(n+1)]
cumsum_val = set()

for i in range(n):
    cumsum[i+1][0] = (cumsum[i][0] + a[i]) % m
    cumsum[i+1][1] = i

cumsum = cumsum[1:]
cumsum.sort()

# ソート前のcumsum[j] > cumsum[i] の場合
ans = cumsum[-1][0]

d = defaultdict(lambda : [n,-1])
nums = set()

# cumsum[i]==num について、添え字の最大と最小をdictで管理する。
for num,i in cumsum:
    d[num][0] = min(d[num][0],i)
    d[num][1] = max(d[num][1],i)
    nums.add(num)

nums = sorted(list(nums))

# 隣り合うnumについて、left[1] > right[0]なら
# ソート前のcumsum[j] < cumsum[i]の組み合わせがある
for i in range(len(nums)-1):
    left = d[nums[i]]
    right = d[nums[i+1]]
    if( left[1] > right[0]):
        ans = max(ans, (nums[i] - nums[i+1])%m )

print(ans)


'''
00223366
12345670
'''
