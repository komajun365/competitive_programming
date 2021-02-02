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

import math

n,d = map(int,input().split())
x,y = map(int,input().split())

if(x%d != 0) or (y%d != 0):
    print(0)
    exit()

x = abs(x//d)
y = abs(y//d)
if(x+y > n) or ((x+y-n)%2 == 1):
    print(0)
    exit()

rem = n-x-y
frac = [0] * (n+1)
for i in range(1,n+1):
    frac[i] = frac[i-1] + math.log(i)
exp4 = math.log(1/4)

ans = 0
rem2 = rem//2
for i in range(rem2+1):
    xp = x + i
    xm = i
    yp = y + rem2 - i
    ym = rem2 - i
    tmp = exp4 * n
    tmp += frac[n] - frac[xp] - frac[n-xp]
    tmp += frac[n-xp] - frac[xm] - frac[n-xp-xm]
    tmp += frac[yp+ym] - frac[yp] - frac[ym]
    ans += math.exp(tmp)

print(ans)



