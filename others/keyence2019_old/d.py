# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,m = map(int,input().split())
a = set(map(int,input().split()))
b = set(map(int,input().split()))

mod = 10**9 + 7

## nCkのmodを求める関数
# テーブルを作る(前処理)
max = n*m +10
fac, finv, inv = [0]*max, [0]*max, [0]*max

def comInit(max):
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1

    for i in range(2,max):
      fac[i] = fac[i-1]* i% mod
      inv[i] = mod - inv[mod%i] * (mod // i) % mod
      finv[i] = finv[i-1] * inv[i] % mod

comInit(max)

# 二項係数の計算
def com(n,k):
    if(n < k):
        return 0
    if( (n<0) | (k < 0)):
        return 0
    return fac[n] * (finv[k] * finv[n-k] % mod) % mod

ab = []
check = set()
for i in a:
    check.add(i)
    if(i in b):
        ab.append((i,'ab'))
    else:
        ab.append((i,'a'))
for i in b:
    check.add(i)
    if(not i in a):
        ab.append((i,'b'))

ab.sort()

if(len(check) != len(ab))|(len(a) != n)|(len(b) !=m):
    print(0)
    exit()

col = 0
row = 0
used = 0
ans = 1

for tmp in ab:
    i,s = tmp
    x = i-used
    ab_flag = 0
    if(s=='a'):
        y = m - row
        col += 1
    elif(s=='b'):
        y = n - col
        row += 1
    else:
        y = (n-col) + (m-row) - 1
        col += 1
        row += 1
        ab_flag = 1
    used += y
    # print('{} {} {} {}'.format(i,used,x,y))
    if(i < used):
        print(0)
        exit()
    if(col==n)|(row==m):
        break

    ans = ans * com(x-1, y-1) * fac[(y-ab_flag)]   % mod

print(ans)
