# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討11分　実装14分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
data = list(map(int,read().split()))

a_nums = set(data[::2])
a_nums.add(0)
a_nums = sorted(list(a_nums))
d = {}
for i,a in enumerate(a_nums):
    d[a] = i

cumsum = [0] * len(a_nums)
for a,b in zip(data[::2],data[1::2]):
    cumsum[d[a]] += b

for i in range(len(cumsum)-1):
    cumsum[i+1] += cumsum[i]

max_calc = [0] * len(a_nums)
max_calc[-1] = cumsum[-1] - a_nums[-1]
for i in range(len(a_nums)-2,0,-1):
    max_calc[i] = max(max_calc[i+1], cumsum[i] - a_nums[i])

ans = 0
for i in range(1,n):
    ans = max(ans, max_calc[i] - cumsum[i-1] + a_nums[i])

print(ans)

'''
大きさiまでの美術品の価値合計をcumsum[i]とする。

a_min~a_max までの美術品を展示するとき、
S-(Amax-Amin) = cumsum[a_max] - cumsum[a_min-1] - (a_max-a_min)
 = (cumsum[a_max] - a_max) - (cumsum[a_min-1] + a_min)

a_minを全探索し、(cumsum[a_max] - a_max)の最大値を取得できればよい。
最大値はセグメント木などで取得すれば、全体をO(NlogN)で計算できる。
今回は右側から計算していくことで、そこより右の最大値を計算した。

'''
