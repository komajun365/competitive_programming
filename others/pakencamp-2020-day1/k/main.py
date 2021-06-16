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

def calc(g,k):
    cnt = 0
    now = 0
    for ai in a:
        now += ai
        if now % g == 0:
            cnt += 1
            now = 0
    
    if now != 0:
        return False
    return cnt >= k

tot = sum(a)
cand = []
for i in range(1,tot+1):
    if tot % i == 0:
        cand.append(i)

ans = []
for k in range(1,n+1):
    tmp = 1
    for g in cand:
        if calc(g,k):
            tmp = g
    ans.append(tmp)

print('\n'.join(map(str,ans)))

