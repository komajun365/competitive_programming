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

n = int(input())
x = input()
mod = 998244353

n2 = n*2
ab = []
for i in range(1,n2,2):
    if(n2%i == 0):
        ab.append([i, n2//i])

coef = [0] * (n2+1)
for a,b in ab:
    dif = b - coef[a]
    coef[a] = dif
    for i in range(a+a,n2,a):
        coef[i] += dif

ans = 0
for a,b in ab:
    l = b//2
    head = x[:l]
    cnt = int(head, 2)
    for i in range(n):
        if (i//l)%2 == 0:
            if x[i] == '0' and head[i%l] == '1':
                break
            elif x[i] == '1' and head[i%l] == '0':
                cnt += 1
                break
        if (i//l)%2 == 1:
            if x[i] == '0' and head[i%l] == '0':
                break
            elif x[i] == '1' and head[i%l] == '1':
                cnt += 1
                break
    else:
        cnt += 1
    
    ans += cnt * coef[a]
    ans %= mod

print(ans)

    
