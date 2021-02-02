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

cs = [0]
cs_max = [0]
tot = 0
for ai in a:
    tot += ai
    cs.append(tot)
    cs_max.append(max(cs_max[-1], tot))

ans = 0
tot = 0
for i in range(1,n+1):
    ans = max(ans, tot + cs_max[i])
    tot += cs[i]
ans = max(ans,tot)

print(ans)
