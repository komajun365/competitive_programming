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
s = input()
d = {'B':0,'W':1,'R':2}
num = [d[si] for si in s]

cnt3 = [0] * (n+1)
mod3 = [1] * (n+1)
for i in range(1,n+1):
    cnt3[i] = cnt3[i-1]
    mod3[i] = mod3[i-1]
    x = i
    while x % 3 == 0:
        cnt3[i] += 1
        x //= 3
    mod3[i] *= x%3
    mod3[i] %= 3

ans = 0
for i in range(n):
    if cnt3[n-1] - cnt3[n-1-i] - cnt3[i] > 0:
        continue
    ans += num[i] * mod3[n-1] * mod3[n-1-i] * mod3[i]
    ans %= 3
     

if n % 2 == 0:
    ans = (ans*-1)%3

color = 'BWR'
print(color[ans])

# print(cnt3)
# print(mod3)