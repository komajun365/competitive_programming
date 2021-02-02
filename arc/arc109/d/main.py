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
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

t,*case = map(int,read().split())

ans = []

def calc(x1,y1,x2,y2,x3,y3):
    xs = [x1,x2,x3]
    ys = [y1,y2,y3]
    xs.sort()
    ys.sort()
    res_x = xs[0]*2
    res_y = ys[0]*2
    if(xs[0] != xs[1]):
        res_x += 1
    if(ys[0] != ys[1]):
        res_y += 1
    return [res_x,res_y]

it = iter(case)
for x1,y1,x2,y2,x3,y3 in zip(it,it,it,it,it,it):
    res_x,res_y = calc(x1,y1,x2,y2,x3,y3)
    dif = max(abs(res_x),abs(res_y))
    if(dif==1):
        if(res_x==-1) and (res_y==-1):
            ans.append(2)
        else:
            ans.append(1)
    elif(dif==0):
        ans.append(0)
    else:
        if(res_x == dif) and (res_y == dif):
            ans.append(dif+1)
        elif(res_x == -dif) and (res_y == -dif):
            ans.append(dif+1)
        else:
            ans.append(dif)

print('\n'.join(map(str,ans)))




