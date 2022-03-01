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
s = list(map(int,input().split()))
t = list(map(int,input().split()))

inf = 10**10
ans = [inf] * n
for i in range(n*2):
    i %= n
    ans[i] = min(ans[i], t[i])
    ans[(i+1) % n] = min(ans[(i+1) % n], ans[i]+s[i])

print('\n'.join(map(str,ans)))