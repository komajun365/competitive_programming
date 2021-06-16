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

r,b = map(int,input().split())
x,y = map(int,input().split())

def calc(a):
    ri = r-a
    bi = b-a
    if ri < 0 or bi < 0:
        return False
    
    a -= ri//(x-1) + bi//(y-1)
    if a > 0:
        return False
    else:
        return True

ok = 0
ng = 10**18
while ng-ok > 1:
    mid = (ok+ng)//2
    if calc(mid):
        ok = mid
    else:
        ng = mid
print(ok)
