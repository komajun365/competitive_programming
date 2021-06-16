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

def sieve(n):
    if( n <= 1):
        return []
    elif(n==2):
        return [2]

    primes = [2]
    len_list = (n+1)//2
    len_sqrt = int(len_list**0.5) + 1
    flags = [True] * len_list
    flags[0] = False
    for i in range(len_sqrt):
        if(flags[i]):
            start = ((i*2+1)**2)//2
            for j in range( start, len_list, i*2+1):
                flags[j] = False
    return [2] + [i*2+1 for i in range(len_list) if flags[i]]

import sys
read = sys.stdin.buffer.read

n,*s = map(int,read().split())

prime_2160 = sieve(2160)
sq = dict()
for i in range(2160, 10**5+1):
    sq[i**2] = i

ans = 0
cnt = dict()
revs = dict()
for si in s:
    factor = []
    for pi in prime_2160:
        cnt_pi = 0
        while si % pi == 0:
            si //= pi
            cnt_pi += 1
        cnt_pi %= 3
        if cnt_pi > 0:
            factor.append([pi,cnt_pi])
        if si == 1:
            break
    
    if si > 10**5 and not si in sq:
        ans += 2
        continue
    if si in sq:
        factor.append([sq[si],2])
    else:
        factor.append([si,1])
    
    num = 1
    num_rev = 1
    for pi, cnt_pi in factor:
        num *= pi ** cnt_pi
        num_rev *= pi ** (3-cnt_pi)
    
    if num == 1:
        if 1 in cnt:
            cnt[1] += 1
        else:
            cnt[1] = 1
    else:
        if num in cnt:
            cnt[num] += 1
        else:
            cnt[num] = 1
            cnt[num_rev] = 0
            revs[num] = num_rev
            revs[num_rev] = num
    


for i in cnt.keys():
    if i == 1:
        ans += 2
        continue

    j = revs[i]
    ans += max(cnt[i], cnt[j])

ans //= 2
print(ans)

# print(cnt)

    




