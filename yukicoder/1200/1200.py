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

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

s = int(readline())
data = list(map(int,read().split()))

def make_divisors(n):
    divisors = []
    for i in range(1,int(n**0.5)+1):
        if(n%i == 0):
            divisors.append(i)
            if(i!= n//i):
                divisors.append(n//i)

    return  divisors

ans = []
it = iter(data)
for x,y in zip(it,it):
    if(x==1)|(y==1):
        ans.append(0)
        continue

    comb = 0
    dif = abs(x-y)
    if(dif==0):
        comb=x-1

        divisors = set(make_divisors(x))
        comb += len(divisors)-1
        if(2 in divisors):
            comb -= 1
        ans.append(comb)
        continue

    divisors = make_divisors(dif)
    for di in divisors:
        xy_sum = x+y
        if(xy_sum%(di+2)!=0):
            continue
        bc_dif = dif//di
        bc_sum = xy_sum//(di+2)
        if(bc_sum<=bc_dif)|((bc_sum-bc_dif)%2==1):
            continue
        comb += 1
    ans.append(comb)

print('\n'.join(map(str,ans)))



'''
x = a*b+c
y = a*c+b
x+y = (b+c)*(a+1)
x-y = (b-c)*(a-1)

x=10
y=12

1,?,?
10,1,1


'''
