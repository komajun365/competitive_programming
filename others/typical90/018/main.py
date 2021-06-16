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
from math import degrees, radians, sin, atan2

t,l,x,y,q,*e = map(int,read().split())

ans = []
for ei in e:
    yi = sin(radians(360 * ei/t + 180)) * (l/2)
    zi = sin(radians(360 * ei/t + 270)) * (l/2) + l/2
    a = (x**2 + (y-yi)**2)**0.5
    tmp = degrees(atan2(zi,a))
    ans.append(str(tmp))
    # print(a,zi)
print('\n'.join(ans))
