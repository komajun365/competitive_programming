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
c = list(map(int,input().split()))

cnt = dict()
num = 0

for i in range(k):
    ci = c[i]
    cnt[ci] = cnt.get(ci, 0) + 1
    if cnt[ci] == 1:
        num += 1

ans = num
for i in range(k,n):
    ci = c[i]
    cnt[ci] = cnt.get(ci, 0) + 1
    if cnt[ci] == 1:
        num += 1
    left = c[i-k]
    cnt[left] -= 1
    if cnt[left] == 0:
        num -= 1
    ans = max(ans,num)
print(ans)