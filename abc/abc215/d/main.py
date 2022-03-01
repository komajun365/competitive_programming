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

n,m = map(int,input().split())
a = list(map(int,input().split()))

l = 10**5 + 1

divs = [-1] * l
for i in range(2,l):
    if divs[i] != -1:
        continue
    for j in range(i,l,i):
        if divs[j] == -1:
            divs[j] = i

primes = set()
for ai in a:
    while ai > 1:
        primes.add(divs[ai])
        ai //= divs[ai]

check = [1] * l
for p in primes:
    for i in range(p,l,p):
        check[i] = 0

ans = []
for i in range(1,m+1):
    if check[i] == 1:
        ans.append(i)

print(len(ans))
if ans:
    print('\n'.join(map(str,ans)))
