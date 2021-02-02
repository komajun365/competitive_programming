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

n = int(input())
s = input()
s += s[0]
ans = [''] * (n+1)
rev_dic = {'S':'W', 'W':'S'}
for a0,a1 in zip('SSWW','SWSW'):
    ans[0] = a0
    ans[1] = a1
    for i in range(1,n):
        if(ans[i] == 'S')&(s[i] == 'o'):
            ans[i+1] = ans[i-1]
        elif(ans[i] == 'S')&(s[i] == 'x'):
            ans[i+1] = rev_dic[ans[i-1]]
        elif(ans[i] == 'W')&(s[i] == 'o'):
            ans[i+1] = rev_dic[ans[i-1]]
        elif(ans[i] == 'W')&(s[i] == 'x'):
            ans[i+1] = ans[i-1]
    if(ans[0] == ans[-1]):
        if(ans[0]=='S')&(s[0]=='o')&(ans[n-1]==ans[1]):
            print(''.join(ans[:-1]))
            exit()
        if(ans[0]=='S')&(s[0]=='x')&(ans[n-1]!=ans[1]):
            print(''.join(ans[:-1]))
            exit()
        if(ans[0]=='W')&(s[0]=='o')&(ans[n-1]!=ans[1]):
            print(''.join(ans[:-1]))
            exit()
        if(ans[0]=='W')&(s[0]=='x')&(ans[n-1]==ans[1]):
            print(''.join(ans[:-1]))
            exit()
print(-1)
