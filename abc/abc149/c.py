# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

x = int(input())

# 約数のリストを作る
# sortはされてないのできをつけよう
def make_divisors(n):
    divisors = []
    for i in range(1,int(n**0.5)+1):
        if(n%i == 0):
            divisors.append(i)
            if(i!= n//i):
                divisors.append(n//i)

    return  divisors

while(True):
    tmp = make_divisors(x)
    if(len(tmp) == 2):
        break
    x += 1

print(x)
