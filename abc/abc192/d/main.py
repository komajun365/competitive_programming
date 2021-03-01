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

x = input()
m = int(input())

if len(x) == 1:
    if m >= int(x):
        print(1)
    else:
        print(0)
    exit()

min_d = 0
for xi in x:
    min_d = max(int(xi),min_d)
min_d += 1

y = 0
for xi in x:
    y = y*min_d + int(xi)
    if y > m:
        print(0)
        exit()

ok = min_d
ng = 10**18 + 1
while(ng-ok > 1):
    mid = (ng+ok)//2
    y = 0
    for xi in x:
        y = y*mid + int(xi)
        if y > m:
            ng = mid
            break
    else:
        ok = mid

print(ok - min_d + 1)
