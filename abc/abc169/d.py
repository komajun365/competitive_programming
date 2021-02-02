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

n = int(input())
if(n==1):
    print(0)
    exit()

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(n**0.5//1)+10 ):
        if(temp%i == 0):
            count=0
            while( temp%i == 0):
                count += 1
                temp = temp // i
            arr.append([i, count])

    if(temp != 1):
        arr.append([temp, 1])

    if(len(arr)==0):
        arr.append([n, 1])

    return arr

arr = factorization(n)

ans = 0
for i,j in arr:
    for k in range(1,100):
        j -= k
        if(j<0):
            break
        ans += 1

print(ans)
