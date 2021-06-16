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

import sys
read = sys.stdin.buffer.read
import math

n,*data = map(int,read().split())
xy = []
it = iter(data)
for x,y in zip(it,it):
    xy.append([x,y])

cnt90 = 0
cnt91 = 0
eps = 0.0000000001

for i in range(n):
    xi,yi = xy[i]
    rad = []
    for j in range(n):
        if i == j:
            continue
        xj,yj = xy[j]
        rad.append(math.atan2(yj-yi, xj-xi))
    rad.sort()
    idx90 = 0
    idx270 = 0
    for j in range(1,n-1):
        while rad[j] - rad[idx90] > math.pi/2 + eps:
            idx90 += 1
        while rad[j] - rad[idx270] > 3*math.pi/2 + eps:
            idx270 += 1
        cnt91 += idx90 - idx270
        if math.pi/2 - eps < rad[j] - rad[idx90] < math.pi/2 + eps:
            cnt90 += 1
        if 3*math.pi/2 - eps < rad[j] - rad[idx270] < 3*math.pi/2 + eps:
            cnt90 += 1
            cnt91 -= 1
    #     print(rad[j] - rad[idx90], rad[j] - rad[idx270])
    #     print(cnt90,cnt91)
    # print(rad)

cnt89 = n * (n-1) * (n-2) // 6
cnt89 -= cnt90 + cnt91
print(cnt89,cnt90,cnt91)







    
