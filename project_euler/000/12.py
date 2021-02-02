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

# 素因数分解
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

    if(temp != 1):
        arr.append([temp, 1])

    if(arr == []):
        arr.append([n, 1])

    res = 1
    for i,j in arr:
        res *= (j+1)

    return res

nm = 1081082
fac_nums = [0] * nm

for i in range(2,nm):
    fac_nums[i] = factorization(i)
    if(i%2==0):
        if(fac_nums[i//2]*fac_nums[i-1] > 500):
            print((i*(i-1))//2)
            exit()
    else:
        if(fac_nums[i]*fac_nums[(i-1)//2] > 500):
            print((i*(i-1))//2)
            exit()
