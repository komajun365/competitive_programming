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

n,l,*xd = read().split()
n = int(n)
l = int(l)

if(xd[1] == 'L'):
    xd = ['0', 'R'] + xd
if(xd[-1] == 'R'):
    xd += [str(l+1),'L']

def calc(rs,ls):
    l = max(rs)
    r = min(ls)
    goal_rs = l
    goal_ls = r
    n_rs = len(rs)
    n_ls = len(ls)
    res = 0
    for rsi in rs:
        res += l-rsi
    for lsi in ls:
        res += lsi-r
    res -= (n_rs * (n_rs-1))//2
    res -= (n_ls * (n_ls-1))//2
    res += max(n_rs,n_ls) * (r-l-1)
    return res

ans = 0
it = iter(xd)
rs = []
ls = []
for x,d in zip(it,it):
    x = int(x)
    if(d=='R') and (len(ls) > 0):
        ans += calc(rs,ls)
        rs = []
        ls = []
    if(d=='R'):
        rs.append(x)
    else:
        ls.append(x)

ans += calc(rs,ls)
print(ans)
