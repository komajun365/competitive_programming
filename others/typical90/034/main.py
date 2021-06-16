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

cnt = dict()
now = 0
ans = 0
l = 0
for r in range(n):
    ar = a[r]
    cnt[ar] = cnt.get(ar,0) + 1
    if cnt[ar] == 1:
        now += 1
    while now > k:
        al = a[l]
        cnt[al] = cnt.get(al,0) - 1
        if cnt[al] == 0:
            now -= 1
        l += 1
    ans = max(ans,r-l+1)
print(ans)