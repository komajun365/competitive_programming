# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

k = int(input())
x,y = map(int,input().split())

if((x+y)%2==1)&(k%2==0):
    print(-1)
    exit()

if(k==1):
    print(x+y)
    a = 0
    b = 0
    while(a!=x):
        a += 1 * ((x>0)*2-1)
        print(' '.join(map(str, [a,b])))
    while(b!=y):
        b += 1 * ((y>0)*2-1)
        print(' '.join(map(str, [a,b])))
    exit()

if(k==2):
    print((x+y)//2)
    a = 0
    b = 0
    if(x%2==1):
        a = (x>0)*2-1
        b = (y>0)*2-1
        print(' '.join(map(str, [a,b])))
    while(a!=x):
        a += 2 * ((x>0)*2-1)
        print(' '.join(map(str, [a,b])))
    while(b!=y):
        b += 2 * ((y>0)*2-1)
        print(' '.join(map(str, [a,b])))
    exit()

sum_xy = x+y
dif_xy = x-y

def print_ans():
    print(len(steps)-1)
    for tmp in steps[-2::-1]:
        a,b = tmp
        print(' '.join(map(str, [(a+b)//2, (a-b)//2])))

steps = []
steps.append([sum_xy,dif_xy])

# cnt = 0
# cnt += 1
# if(cnt>10):
#     print(steps)
#     exit()

while((sum_xy%k)!=0):
    if((k%2==1)&( (abs(sum_xy)%k)%2 ==0)):
        if(sum_xy > 0):
            sum_xy -= k-2
        else:
            sum_xy += k-2
    else:
        if(sum_xy > 0):
            sum_xy -= (sum_xy%k)
        else:
            sum_xy -=  (sum_xy%k) - k

    dif_xy -= k * ((dif_xy>0)*2-1)
    steps.append([sum_xy, dif_xy])

if(sum_xy==0)&(dif_xy==0):
    print_ans()
    exit()

while(dif_xy%k!=0):
    if((k%2==1)&( (abs(dif_xy)%k)%2 ==0)):
        if(dif_xy > 0):
            dif_xy -= k-2
        else:
            dif_xy += k-2
    else:
        if(dif_xy > 0):
            dif_xy -= (dif_xy%k)
        else:
            dif_xy -=  (dif_xy%k) - k

    sum_xy -= k * ((sum_xy>0)*2-1)
    steps.append([sum_xy, dif_xy])


while(sum_xy!=0)|(dif_xy!=0):
    if((abs(sum_xy)==k)&(dif_xy==0))|((dif_xy==0)&(abs(dif_xy==k))):
        sum_xy = 0
        dif_xy = 0
        steps.append([sum_xy, dif_xy])
        break

    sum_xy -= k * ((sum_xy>0)*2-1)
    dif_xy -= k * ((dif_xy>0)*2-1)
    steps.append([sum_xy, dif_xy])

print_ans()
