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

from math import gcd

n,x,d = map(int,input().split())
if x == 0 and d == 0:
    print(1)
    exit()
if x == 0:
    ans = n*(n-1)//2 + 1
    print(ans)
    exit()
if d == 0:
    print(n+1)
    exit()

x0 = abs(x)
d0 = abs(d)
a = d0 // gcd(d0,x0)

ans = 0
for i in range(min(a,n+1)):
    lr = []
    for j in range(i,n+1,a):
        dx = (j // a) * x * a // d
        l = j * (j-1)//2 + dx
        r = j * (n-1+n-j)//2 + 1 + dx
        lr.append([l,r])
    lr.sort(key=lambda z: z[0]*-1)
    # print(i,lr)

    while lr:
        l,r = lr.pop()
        while lr:
            if lr[-1][0] <= r:
                l2,r2 = lr.pop()
                r = max(r,r2)
            else:
                break
        ans += r-l

print(ans)




'''
xをi個取るとき、
dを(i)(i-1)//2 ~ i(n-1 + n-i)//2 個取れる

被りがやばい
ax = 0 (mod d) みたいなケースを考える
a = d / gcd(x,d)


'''