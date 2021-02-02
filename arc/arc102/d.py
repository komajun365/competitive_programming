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

l = int(input())
bits = []
x = l
while(x>0):
    bits.append(x%2)
    x //= 2

ans = []
n = len(bits)
for i in range(1,n):
    ans.append('{} {} {}'.format(i,i+1,0))
    ans.append('{} {} {}'.format(i,i+1,2**(n-i-1)))

base = 2**(n-1)
for i,bi in enumerate(bits[:-1]):
    if(bi==1):
        ans.append('{} {} {}'.format(1,n-i,base))
        base += 2**i

print('{} {}'.format(n,len(ans)))
print('\n'.join(ans))
