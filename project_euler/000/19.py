# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('p018_triangle.txt', 'r')
sys.stdin = f

y = 1900
m = 1
now = 1

ans = 0
while(y<2001):
    if(now==0)&(y>1900):
        ans += 1
        # print(y,m)

    if(m in [4,6,9,11]):
        now += 30
        now %= 7
    if(m in [1,3,5,7,8,10,12]):
        now += 31
        now %= 7
    if(m==2):
        now += 28
        if(y%4==0):
            now+=1
        if(y%100==0):
            now-=1
        if(y%400==0):
            now+=1
        now %= 7

    if(m==12):
        y+=1
        m=1
    else:
        m += 1


print(ans)
print(y,m,now)

# こっちのほうが楽ですね
import datetime
ans = 0
for i in range(1901,2001):
    for j in range(1,13):
        dt = datetime.datetime(i,j,1)
        if(dt.weekday()==6):
            ans += 1
print(ans)
