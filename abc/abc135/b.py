# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
p = list(map(int,input().split()))

ex = list(range(1,n+1))

for i in range(n):
    for j in range(n):
        tmp = p.copy()
        tmp_i = tmp[i]
        tmp[i] = tmp[j]
        tmp[j] = tmp_i
        for k in range(n):
            cnt = 0
            if(ex[k] != tmp[k]):
                cnt += 1
                break
        if(cnt == 0):
            print('YES')
            exit()

print('NO')
