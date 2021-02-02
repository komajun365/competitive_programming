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
f = open('../../input.txt', 'r')
sys.stdin = f

s = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
n = len(s)

now = 0
for i in range(n):
    print(i,now)
    for top in range(3):
        flag = False
        tmp = now + top * (3**i)
        print(tmp)
        for j in range(i+1):
            if(s[j] == 'D'):
                if(tmp%3==0):
                    tmp //= 3
                else:
                    break
            elif(s[j] == 'U'):
                if(tmp%3==1):
                    tmp = (4*tmp+2)//3
                else:
                    break
            else:
                if(tmp%3==2):
                    tmp = (2*tmp-1)//3
                else:
                    break
        else:
            now = now + top * (3**i)
            flag=True
        if(flag):
            break

while(now < 10**15):
    now += 3**n

print(now)    


'''
D
3で割る

U
a(n) = (3x+1)として
a(n+1) = (12x+6)//3 = 4X+2

d
a(n) = (3x+2)として
a(n+1) = (6x+3)//3 = 2X+1

Ud: 9x+1
dd: 9x+8
dU: 9x+2
Ud: 9x+4

Dd: 9x+6
UD: 9x+4

'''
