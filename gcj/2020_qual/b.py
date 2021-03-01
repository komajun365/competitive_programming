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
read = sys.stdin.read

n,*data = read().split()
n = int(n)

ans = [0] * n
for i in range(n):
    s = data[i]
    res = ''
    d = 0
    for si in s:
        num = int(si)
        if d < num:
            res += '(' * (num-d)
        elif d > num:
            res += ')' * (d-num)
        res += si
        d = num
    res += ')' * d

    ans[i] = 'Case #{}: {}'.format(i+1,res[::])

print('\n'.join(ans))
