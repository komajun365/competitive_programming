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
f = open('p042_words.txt', 'r')
sys.stdin = f

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(n**0.5//1)+1 ):
        if(temp%i == 0):
            count=0
            while( temp%i == 0):
                count += 1
                temp = temp // i
            arr.append([i, count])
        if temp==1:
            break

    if(temp != 1):
        arr.append([temp, 1])
    
    return arr

n = 1000000
cnt = 0
for i in range(2,n):
    arr = factorization(i)
    if len(arr) == 4:
        cnt += 1
    else:
        cnt = 0
    if cnt == 4:
        print(i-3,i)



















