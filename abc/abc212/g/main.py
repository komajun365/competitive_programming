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

p = int(input())
mod = 998244353
if p==2:
    print(2)
    exit()

def make_divisors(n):
    divisors = []
    for i in range(1,int(n**0.5)+1):
        if(n%i == 0):
            divisors.append(i)
            if(i!= n//i):
                divisors.append(n//i)

    return  divisors

divs = make_divisors(p-1)
divs.sort()
l = len(divs)
nums = [0] * l

ans = 1
cnt = [0] * l
for i in range(l-1,-1,-1):
    di = divs[i]
    base = (p-1) // di
    cnt[i] = base
    for j in range(i+1,l):
        if divs[j] % di == 0:
            cnt[i] -= cnt[j]
    ans += base * cnt[i]
    ans %= mod

print(ans)

# print(divs)
# print(cnt)




