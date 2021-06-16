# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

import sys
read = sys.stdin.buffer.read

k,q,*data = map(int,read().split())
d = data[:k]
nxm = data[k:]

def solve(n,x,m):
    cs = [0]
    cnt0 = [0]
    for i in range(k):
        di = d[i] % m
        cs.append(cs[-1] + di)
        cnt0.append(cnt0[-1] + 1 * (di==0))
    
    cyc,rem = divmod(n-1, k)
    tot = x%m + cs[-1] * cyc + cs[rem]
    res = n-1 - tot//m - (cnt0[-1] * cyc + cnt0[rem])

    # print(cyc,rem,tot)
    # print(cs)
    # print(cnt0)
    return res


ans = []
it = iter(nxm)
for n,x,m in zip(it,it,it):
    ans.append(solve(n,x,m))

print('\n'.join(map(str,ans)))

'''
x1 ... xn
mod しなければ0でない限り上がり続けるが、
modするとxn//mod 回下がる

'''