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

n,k = map(int,input().split())
a = list(map(int,input().split()))

m = max(a)
tot = sum(a)
if m*n - tot <= k:
    k -= m*n - tot
    ans = m + k//n
    print(ans)
    exit()

cnt = [0] * (m+1)
for ai in a:
    cnt[ai] += 1
for i in range(m):
    cnt[i+1] += cnt[i]

lim = min(m,int(m**0.5)+2)

cost = m*n - tot
for i in range(m,lim,-1):
    for j in range(-(-m//i)):
        j += 1
        cost -= (cnt[min(m,j*i)] - cnt[min(m,(j-1)*i)]) * j
        cost += (cnt[min(m,j*i)] - cnt[min(m,j*(i-1))]) * (i-1)
    if cost <= k:
        print(i-1)
        exit()
    # print(m,lim,i,cost)

for i in range(lim,0,-1):
    cost = 0
    for ai in a:
        cost += (-ai) % i
    if cost <= k:
        print(i)
        exit()


