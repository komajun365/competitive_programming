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
read = sys.stdin.buffer.read

n,*data = map(int,read().split())
at = data[:2*n]
q = data[2*n]
x = data[2*n+1:]

inf = 10 ** 18
lr = [-inf, inf]
for i in range(n-1,-1,-1):
    a,t = at[i*2:i*2+2]
    if t == 1:
        lr[0] -= a
        lr[1] -= a
    elif t == 2:
        lr[0] = max(lr[0], a)
    else:
        lr[1] =min(lr[1], a)

def calc(x):
    for i in range(n):
        a,t = at[i*2:i*2+2]
        if t == 1:
            x += a
        elif t == 2:
            x = max(x, a)
        else:
            x =min(x, a)
    return x

ans = []
if lr[0] >= lr[1]:
    ans = [calc(0)] * q
else:
    l_ans = calc(lr[0])
    r_ans = calc(lr[1])
    for xi in x:
        if xi <= lr[0]:
            ans.append(l_ans)
        elif xi >= lr[1]:
            ans.append(r_ans)
        else:
            ans.append(l_ans + (xi - lr[0]))

print('\n'.join(map(str,ans)))

