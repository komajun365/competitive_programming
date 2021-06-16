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

n,l = map(int,input().split())
k = int(input())
a = [0] + list(map(int,input().split())) + [l]

def cut(x):
    l = 0
    cnt = 0
    for i in range(1,n+2):
        if a[i] - a[l] >= x:
            cnt += 1
            l = i
    return cnt >= k+1

ok = 0
ng = l+1
while ng-ok > 1:
    mid = (ng+ok)//2
    if cut(mid):
        ok = mid
    else:
        ng = mid
print(ok)


