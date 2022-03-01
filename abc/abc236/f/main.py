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
c = list(map(int, input().split()))

cb = [i + (ci<<30) for i,ci in enumerate(c,1)]
mask = (1<<30) - 1

cb.sort()

def get_base(x,basis):
    for b in basis:
        x = min(x,x^b)
    return x

ans = 0
basis = []
for cbi in cb:
    bi = cbi & mask
    ci = cbi >> 30
    for b in basis:
        bi = min(bi,bi^b)
    if bi != 0:
        ans += ci
        basis.append(bi)

print(ans)
