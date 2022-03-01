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

k = int(input())

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
        if temp==1:
            break

    if(temp != 1):
        arr.append([temp, 1])
    
    return arr

def com(x):
    x += 2
    res = x * (x-1) //2
    return res

arr = factorization(k)
ans = 1
for _,x in arr:
    ans *= com(x)

#a==b or b==c,a==b==cのとき
for i in range(1,10**6+1):
    xy = i**2
    if k % xy != 0:
        continue
    z = k //xy
    if i == z:
        ans += 5
    else:
        ans += 3
ans //= 6
print(ans)
