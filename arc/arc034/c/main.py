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

a,b = map(int,input().split())
mod = 10**9+7

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

fac = dict()
for i in range(b+1,a+1):
    arr = factorization(i)
    for p,num in arr:
        if p in fac:
            fac[p] += num
        else:
            fac[p] = num

ans = 1
for i in fac.values():
    ans *= (i+1)
    ans %= mod
print(ans)