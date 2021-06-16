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
# f = open('../../input.txt', 'r')
# sys.stdin = f

t,a,b = map(int,input().split())
width = 10**9

def search(x,y):
    print('{} {}'.format(x,y), flush=True)
    return input()

def solve():
    for x0,y0 in zip([0,-1*width//2,-1*width//2,width//2,width//2],
                     [0,-1*width//2,width//2,-1*width//2,width//2]):
        res = search(x0,y0)
        if res == 'CENTER':
            return 1
        if res == 'HIT':
            break
    
    ok,ng = x0,width+1
    while ng-ok > 1:
        mid = (ng+ok)//2
        res = search(mid,y0)
        if res == 'CENTER':
            return 1
        if res == 'HIT':
            ok = mid
        else:
            ng = mid
    xr = ok

    ok,ng = x0,-1*width-1
    while ok-ng > 1:
        mid = (ng+ok)//2
        res = search(mid,y0)
        if res == 'CENTER':
            return 1
        if res == 'HIT':
            ok = mid
        else:
            ng = mid
    xl = ok
    
    ok,ng = y0,width+1
    while ng-ok > 1:
        mid = (ng+ok)//2
        res = search(x0,mid)
        if res == 'CENTER':
            return 1
        if res == 'HIT':
            ok = mid
        else:
            ng = mid
    yr = ok

    ok,ng = y0,-1*width-1
    while ok-ng > 1:
        mid = (ng+ok)//2
        res = search(x0,mid)
        if res == 'CENTER':
            return 1
        if res == 'HIT':
            ok = mid
        else:
            ng = mid
    yl = ok

    x = (xl+xr)//2
    y = (yl+yr)//2
    res = search(x,y)
    return 1

for _ in range(t):
    solve()

exit()