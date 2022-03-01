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
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

a.sort()
b.sort()
c.sort()

ai,bi,ci = 0,0,0
ans = 0
while ai < n and bi < n and ci < n:
    while bi < n:
        if a[ai] >= b[bi]:
            bi += 1
        else:
            break
    if bi == n:
        break
    while ci < n:
        if b[bi] >= c[ci]:
            ci += 1
        else:
            break
    if ci == n:
        break
    ai += 1
    bi += 1
    ci += 1
    ans += 1

print(ans)
