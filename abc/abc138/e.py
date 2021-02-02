# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

s = input()
t = input()
len_s = len(s)

import bisect
point_dic = {}
for i in range(26):
    alp = chr( ord('a') + i )
    point_dic[alp] = []

for i in range(len_s):
    i_alp = s[i]
    point_dic[i_alp].append(i+1)

now = 1
cycle = 0
for i in t:
    points = point_dic[i]
    if(len(points) == 0):
        print(-1)
        exit()
    tmp = bisect.bisect_left(points, now)
    if(tmp == len(points)):
        now = points[0]+1
        cycle += 1
    else:
        now = points[tmp]+1

ans = cycle * len_s + now - 1
print(ans)

# abbaabb
# [1,4,5]
# [2,3,6,7]
# ababb
# now = 1-2-3-5-7-8
