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
readline = sys.stdin.readline

n = int(readline())
s = readline().strip()
ans = list(s)
q,*tab = map(int,read().split())

it = iter(tab)
q2 = 0
for t,a,b in zip(it,it,it):
    a = (a-1 + q2) % (2*n)
    b = (b-1 + q2) % (2*n)
    if t == 1:
        ans[a],ans[b] = ans[b],ans[a]
    else:
        q2 += n
        q2 %= (2*n)

if q2 == n:
    ans = ans[n:] + ans[:n]

print(''.join(ans))
