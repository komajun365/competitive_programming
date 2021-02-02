import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,m = map(int, input().split())
sc = [list(map(int,input().split())) for _ in range(m)]

ans = [-1] * n
for s,c in sc:
    if(ans[s-1] != -1):
        if(ans[s-1] != c):
            print(-1)
            exit()

    if(n>1)&(s==1)&(c==0):
        print(-1)
        exit()
    ans[s-1] = c

ans_num = 0
for i,num in enumerate(ans[::-1]):
    if(num == -1):
        if(i==n-1)&(n!=1):
            ans_num += 1*10**(i)
        continue

    ans_num += num * 10**(i)

print(ans_num)
