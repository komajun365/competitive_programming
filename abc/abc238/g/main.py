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

def sieve(n):
    if( n <= 1):
        return []
    elif(n==2):
        return [2]

    primes = [2]
    primes_append = primes.append
    len_list = (n+1)//2
    flags = [True] * len_list
    flags[0] = False
    for i in range(len_list):
        if(flags[i]):
            primes_append(i*2+1)
            start = ((i*2+1)**2)//2
            for j in range( start, len_list, i*2+1):
                flags[j] = False
    return primes

n,q,*data = map(int,read().split())
a = data[:n]
lr = data[n:]

primes = sieve(1000)
ok = list(range(q))
for p in primes:
    cnt = [0]*(n+1)
    for i in range(n):
        cnt[i+1] += cnt[i]
        while a[i] % p == 0:
            cnt[i+1] += 1
            a[i] //= p
    
    ok2 = []
    for j in ok:
        lj,rj = lr[j*2:j*2+2]
        if (cnt[rj] - cnt[lj-1]) % 3 == 0:
            ok2.append(j)
    ok,ok2 = ok2,ok

rems = dict()
for i,ai in enumerate(a):
    if ai != 1:
        rems[ai] = rems.get(ai,[]) + [i]

keys = list(rems.keys())
batch = 64 * 32
cycle = -(-len(keys)//batch)

for i in range(cycle):
    head = i * batch
    size = min(len(keys), (i+1)*batch) - head
    c0 = [0] * (n+1)
    c1 = [0] * (n+1)
    c2 = [0] * (n+1)
    c0[0] = (1<<size) - 1
    for j in range(size):
        num = keys[j+head]
        case = 0
        for idx in rems[num]:
            idx += 1
            if case == 0:
                c0[idx] ^= (1 << j)
                c1[idx] ^= (1 << j)
                case = 1
            elif case == 1:
                c1[idx] ^= (1 << j)
                c2[idx] ^= (1 << j)
                case = 2
            else:
                c2[idx] ^= (1 << j)
                c0[idx] ^= (1 << j)
                case = 0
    
    for j in range(n):
        c0[j+1] ^= c0[j]
        c1[j+1] ^= c1[j]
        c2[j+1] ^= c2[j]
    
    ok2 = []
    for j in ok:
        lj,rj = lr[j*2:j*2+2]
        b0 = c0[rj+1] & c0[lj]
        b1 = c1[rj+1] & c1[lj]
        b2 = c2[rj+1] & c2[lj]
        if b0 ^ b1 ^ b2 == 0:
            ok2.append(j)
    ok,ok2 = ok2,ok

ans = ['No'] * q
for i in ok:
    ans[i] = 'Yes'
print(*ans, sep='\n')




