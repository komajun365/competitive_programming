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

import itertools

n = int(input())
a = list(map(int,input().split()))
mod = 10**9+7

max_n = 50
fac, finv, inv = [0]*max_n, [0]*max_n, [0]*max_n

def comInit(max_n):
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1

    for i in range(2,max_n):
      fac[i] = fac[i-1]* i% mod
      inv[i] = mod - inv[mod%i] * (mod // i) % mod
      finv[i] = finv[i-1] * inv[i] % mod

comInit(max_n)

def com(n,k):
    if(n < k):
        return 0
    if( (n<0) | (k < 0)):
        return 0
    res = finv[k]
    for i in range(n,n-k,-1):
        res *= i
        res %= mod
    return res

def calc_comb(num_max):
    l = len(num_max)
    res = 0
    for i in range(1 << (l-1)):
        left = 0
        cnt = 0
        tmp = 1
        for j in range(l):
            if (i >> j) & 1:
                cnt += 1
            else:
                rl = j+1 - left
                tmp *= com(num_max[left] - 1 + rl, rl)
                tmp %= mod
                left = j+1
        if cnt % 2 == 0:
            res += tmp
        else:
            res -= tmp
        res %= mod
    return res


cnt = []
tmp = [[]]
while tmp:
    tmp2 = []
    while tmp:
        x = tmp.pop()
        for i in range(1,n - sum(x)):
            tmp2.append(x + [i])
        cnt.append(x + [n - sum(x)])
    tmp,tmp2 = tmp2,tmp

ans = 0
done = set()
for ci in cnt:
    nums = []
    for v,k in enumerate(ci):
        nums += [v] * k
    
    for p in itertools.permutations(nums):
        p = tuple(p)
        if p in done:
            continue
        done.add(p)

        lis = []
        for pi in p:
            for j in range(len(lis)):
                if lis[j] >= pi:
                    lis[j] = pi
                    break
            else:
                lis.append(pi)
        
        l = max(p)+1
        num_max = [10**9] * l
        for i in range(n):
            num_max[p[i]] = min(num_max[p[i]], a[i])
        
        for i in range(l-1,0,-1):
            num_max[i-1] = min(num_max[i-1], num_max[i]-1)
        if num_max[0] <= 0:
            continue

        ans += calc_comb(num_max) * len(lis)
        ans %= mod

for ai in a:
    ans *= pow(ai,mod-2,mod)
    ans %= mod

print(ans)