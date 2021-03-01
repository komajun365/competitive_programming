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

a.sort(reverse=True)
a.append(0)

for x in range(1,n+1):
    if a[x] <= x:
        break

ans = 0
if a[x] == x:
    for i in range(n-1,-1,-1):
        if a[i] == x:
            ans |= (i - (x-1)) % 2
            break

if a[x-1] > x:
    ans |= (a[x-1] - x) % 2

if ans:
    print('First')
else:
    print('Second')




