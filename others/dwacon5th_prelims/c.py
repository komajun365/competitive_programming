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

n = int(input()) + 1
s = '?' + input()
q = int(input())
k = list(map(int,input().split()))

p_d = []
cnt_m = [0]*n
cnt_c = [0]*n

for i,si in enumerate(s[1:],1):
    cnt_m[i] = cnt_m[i-1]
    cnt_c[i] = cnt_c[i-1]
    if(si=='D'):
        p_d.append(i)
    elif(si=='M'):
        cnt_m[i] += 1
    elif(si=='C'):
        cnt_c[i] += 1

left_c = [0]*n
for i in range(1,n):
    left_c[i] = left_c[i-1]
    if(s[i]=='M'):
        left_c[i] += cnt_c[i]

# print(cnt_m)
# print(cnt_c)
# print(left_c)

ans = []
for ki in k:
    tmp = 0
    for di in p_d:
        x = cnt_m[min(di+ki-1,n-1)] - cnt_m[di-1]
        y = cnt_c[min(di+ki-1,n-1)]
        tmp += x*y - left_c[min(di+ki-1,n-1)] + left_c[di-1]
    ans.append(tmp)

print('\n'.join(map(str,ans)))





'''

s[a1] == D,s[a2] == D のとき



'''
