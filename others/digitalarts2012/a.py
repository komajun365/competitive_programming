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

s = input().split()
n = int(input())
t = [input() for _ in range(n)]

len_s = len(s)
ans = [''] * len_s

def check(si):
    for j in range(n):
        tj = t[j]
        if(len(si) != len(tj)):
            continue

        for a,b in zip(si,tj):
            if(b != '*')&(a!=b):
                break
        else:
            return '*' * len(si)

    return si

for i in range(len_s):
    si = s[i]
    ans[i] = check(si)

print(' '.join(ans))
