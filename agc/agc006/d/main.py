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

n = int(input())
a = list(map(int,input().split()))

n2 = n*2-1
m = n-1

# 答えはx以上か？
def check(x):
    ln,rn = -1,-1
    for l in range(m,0,-1):
        if a[l] >= x and a[l-1] >= x:
            ln = 1
            break
        if a[l] < x and a[l-1] < x:
            ln = 0
            break
    
    for r in range(m,n2-1):
        if a[r] >= x and a[r+1] >= x:
            rn = 1
            break
        if a[r] < x and a[r+1] < x:
            rn = 0
            break
    
    if ln != -1 and rn != -1:
        l = m-l
        r = r-m
        if l < r:
            return ln
        else:
            return rn
    elif ln != -1:
        return ln
    elif rn != -1:
        return rn
    else:
        return a[0] >= x

ok = 1
ng = n2+1 
while ng-ok > 1:
    mid = (ok+ng)//2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)

