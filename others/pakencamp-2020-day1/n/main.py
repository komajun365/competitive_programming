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

ll = 0
rr = n-1
for i in range(1,n):
    if a[i] < a[i-1]:
        lr = i-1
        break
else:
    print(0)
    exit()

for i in range(n-1,0,-1):
    if a[i] < a[i-1]:
        rl = i
        break

ans = a[ll] + a[rl]
for i in range(rl,n):
    if a[i] > a[lr]:
        ans = min(ans, a[lr+1] + a[i])
        break
else:
    i += 1
ans = min(ans, a[lr+1] + a[i-1])

print(ans)
