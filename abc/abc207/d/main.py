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

it = iter(data)
abcd = [[x,y] for x,y in zip(it,it)]
ab = abcd[:n]
cd = abcd[n:]

eps = 10**(-5)

if n == 1:
    print('Yes')
    exit()
elif n == 2:
    d1 = (ab[0][0] - ab[1][0])**2 + (ab[0][1] - ab[1][1])**2
    d2 = (cd[0][0] - cd[1][0])**2 + (cd[0][1] - cd[1][1])**2
    if d1 == d2:
        print('Yes')
    else:
        print('No')
    exit()

def go_0(points, i):
    dif_x,dif_y = points[i]

    res = []
    res_set = set()
    for j in range(n):
        x,y = points[j]
        res.append([x-dif_x, y-dif_y])
        res_set.add((x-dif_x, y-dif_y))
    return res,res_set

i = 0
ab0,_ = go_0(ab,i)
for j in range(n):
    cd0,cd0_set = go_0(cd,j)

    k = 1
    x0,y0 = ab0[k]

    for l in range(n):
        x1,y1 = cd0[l]
        if x0**2+y0**2 != x1**2+y1**2:
            continue
        
        theta = math.atan2(y1,x1) - math.atan2(y0,x0)
        # cos = (x0*x1 + y0*y1) / (x0**2 + y0**2)**0.5 *  (x1**2 + y1**2)**0.5
        
        for m in range(n):
            if m == i or m == k:
                continue
            x2,y2 = ab0[m]
            x3 = x2 * math.cos(theta) - y2 * math.sin(theta)
            y3 = y2 * math.cos(theta) + x2 * math.sin(theta)
            x4,y4 = round(x3),round(y3)
            if abs(x3-x4) > eps or abs(y3-y4) > eps:
                break

            if not (x4,y4) in cd0_set:
                break
        else:
            print('Yes')
            exit()

print('No')


# for i in range(n):
#     ab0,_ = go_0(ab,i)
#     for j in range(n):
#         cd0,cd0_set = go_0(cd,i)

#         k = 0 if i != 0 else 1
#         x0,y0 = ab0[k]

#         for l in range(n):
#             x1,y1 = cd0[l]
#             if x0**2+y0**2 != x1**2+y1**2:
#                 continue
            
#             theta = math.atan2(y1,x1) - math.atan2(y0,x0)
#             # cos = (x0*x1 + y0*y1) / (x0**2 + y0**2)**0.5 *  (x1**2 + y1**2)**0.5
            
#             for m in range(n):
#                 if m == i or m == k:
#                     continue
#                 x2,y2 = ab0[m]
#                 x3 = x2 * math.cos(theta) - y2 * math.sin(theta)
#                 y3 = y2 * math.cos(theta) + x2 * math.sin(theta)
#                 x4,y4 = round(x3),round(y3)
#                 if abs(x3-x4) > eps or abs(y3-y4) > eps:
#                     break

#                 if not (x4,y4) in cd0_set:
#                     break
#             else:
#                 print('Yes')
#                 exit()

# print('No')












'''
Sのどれかを原点にする
Tのどれかを原点にする

Sの原点ではない点を取って、
Tの点と重ねられるか考える

重ねられるなら、他の点も回転させて、一致点があるかどうか見る


100**4だけど枝刈りが聞くだろう。
'''