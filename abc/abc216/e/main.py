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

def calc(x):
    res = 0
    for ai in a:
        res += max(0, ai-x)
    return res

def add(x):
    res = 0
    for ai in a:
        if ai <= x:
            continue
        res += (ai-x) * (ai + x + 1) //2
    return res

if sum(a) <= k:
    print(add(0))
    exit()

ng = 0
ok = 2*10**9
while ok-ng > 1:
    mid = (ok+ng)//2
    if calc(mid) >= k:
        ng = mid
    else:
        ok = mid

ans = add(ok) + ok * (k-calc(ok))
print(ans) 




# from heapq import heappop,heappush

# n,k = map(int,input().split())
# a = list(map(int,input().split()))

# hq = []
# for ai in a:
#     heappush(hq,ai*-1)

# ans = 0
# for _ in range(k):
#     x = heappop(hq) * -1
#     ans += max(x,0)
#     x -= 1
#     heappush(hq, x*-1)
# print(ans)
