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

import sys
read = sys.stdin.read

n,*pqr = read().split()

ans = ''
it = iter(pqr)
for p,q,r in zip(it,it,it):
    if p == 'BEGINNING':
        ans += r[0]
    elif p == 'END':
        ans += r[-1]
    else:
        l = len(r)
        ans += r[l//2]
print(ans)