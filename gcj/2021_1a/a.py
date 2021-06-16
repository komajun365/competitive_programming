# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read

t,*data = map(int,read().split())
t = int(t)

def solve(n,x):
    res = 0
    now = x[0]
    for i in range(1,n):
        if now < x[i]:
            now = x[i]
            continue

        s1 = str(now)
        s2 = str(x[i])
        if len(s1) == len(s2):
            now = x[i] * 10
            res += 1
            continue

        s1_head = int(s1[:len(s2)])
        if s1_head > x[i]:
            add = len(s1)-len(s2)+1
            now = x[i] * pow(10, add )
            res += add
        elif s1_head < x[i]:
            add = len(s1)-len(s2)
            now = x[i] * pow(10, add )
            res += add
        else:        
            s1_tail = s1[len(s2):]
            if s1_tail.count('9') == len(s1_tail):
                add = len(s1)-len(s2)+1
                now = x[i] * pow(10, add )
                res += add
            else:
                add = len(s1)-len(s2)
                now = now + 1
                res += add
    return res

ans = [''] * t
idx = 0
for i in range(t):
    n = data[idx]
    x = data[idx+1:idx+1+n]
    idx += n+1
    res = solve(n,x)
    ans[i] = 'Case #{}: {}'.format(i+1,res)
print('\n'.join(ans))

