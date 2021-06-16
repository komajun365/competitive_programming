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

'''
O(N**2)で解きたい。
2点x,yを決めて、3点目を点zとする。
zと反対側の弧でx,yの中点mを取ると、
zはmを中心としたx,yを通る円の円周上に現れる。

しかも2倍角の公式を考えると良い感じの角度の間隔で現れる。
ので、円周上の複数の点の重心を上手くO(1)で更新していけばよさそう。

'''

import sys
read = sys.stdin.buffer.read
import math

n,l,*t = map(int,read().split())
l *= 4
t = [i*4 for i in t]

ans_x = 0
ans_y = 0
for i in range(n-2):
    gx = 0
    gy = 0
    cnt = 0
    for j in range(i+2,n):
        # iとjの中点 iの極座標を0とする。
        m = (t[j] - t[i] + l) // 2 % l

        # 増えた頂点を加算
        k = t[j-1]-t[i]
        gx += math.cos(math.pi * k / l)
        gy += math.sin(math.pi * k / l)
        cnt += 1

        # ansに加算
        rad =  math.pi * 2 * ((t[i] + (t[j]-t[i])//4) % l) / l
        r = 2 * math.sin((math.pi * 2*(l-m)/2)/l)
        ans_x += (gx * math.cos(rad) - gy * math.sin(rad)) * r
        ans_y += (gx * math.sin(rad) + gy * math.cos(rad)) * r
        # print(ans_x, ans_y)
        rad_m = math.pi * 2 * ((t[i]+m)%l) / l
        ans_x += cnt * math.cos(rad_m)
        ans_y += cnt * math.sin(rad_m)
        # print(m,k,gx,gy, rad, rad_m, r)
        # print(ans_x, ans_y)

ans_x /= n*(n-1)*(n-2)/6
ans_y /= n*(n-1)*(n-2)/6

print(ans_x,ans_y)

# print(math.sin(math.radians(22.5)))



