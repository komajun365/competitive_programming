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
readline = sys.stdin.readline
readlines = sys.stdin.readlines

s = readline().strip()
t = readline().strip()
q = int(readline())
abcd = list(map(int,read().split()))

cumsum_s = [0] * (len(s)+1)
cumsum_t = [0] * (len(t)+1)
for cs,st in zip([cumsum_s,cumsum_t],[s,t]):
    for i,ch in enumerate(st,1):
        cs[i] = cs[i-1] + (1 if ch=='A' else 2)

ans = []
it = iter(abcd)
for a,b,c,d in zip(it,it,it,it):
    num1 = cumsum_s[b] - cumsum_s[a-1]
    num2 = cumsum_t[d] - cumsum_t[c-1]
    if((num1-num2)%3 == 0):
        ans.append('YES')
    else:
        ans.append('NO')

print('\n'.join(ans))




'''
A,BB,AAB,BAA

A,BB,AAAA,ABBBBA,ABA

AA-B
ABABA - AAAAAAA

'''
