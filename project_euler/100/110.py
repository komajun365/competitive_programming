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

primes = sieve(1000)

tmp_max = 1
fac = 1
for i,ex in enumerate([10,6,4,3,2,2,2,2]):
    tmp_max *= primes[i]**ex
    fac *= ex*2+1

print(tmp_max)
print(fac)

def calc_n(lis):
    res = 1
    for i,ex in enumerate(lis):
        res *= primes[i]**ex
    return res

def calc_fn(lis):
    res = 1
    for ex in lis:
        res *= ex*2 + 1
    return res

from heapq import heappop,heappush
# from collections import defaultdict
# d = defaultdict(int)

done = set()
hq = []
for i in range(1,100):
    if(3**i > 8*10**6):
        break
    lis = [1] * i
    n = calc_n(lis)
    heappush(hq, (n,lis))
    done.add(n)

cnt = 0
cnt2 = 0
for _ in range(100000):
    n,lis = heappop(hq)
    fn = calc_fn(lis)
    if(fn > 8*10**6):
        ans_lis = lis
        print(_)
        print(cnt)
        print(cnt2)

        break
    for i in range(len(lis)):
        n_lis = lis[::]
        if(i==0):
            n_lis[0] += 1
        else:
            if(n_lis[i] == n_lis[i-1]):
                continue
            n_lis[i] += 1
        n_n = calc_n(n_lis)
        cnt2 += 1
        if(not n_n in done):
            cnt += 1
            heappush(hq,(n_n, n_lis))
            done.add(n_n)


print(hq[:5])

print(ans_lis)
ans = 1
for i,ex in enumerate(ans_lis):
    ans *= primes[i]**ex
print(ans)





'''
1/x + 1/y = 1/n

yn + xn = xy
n(x+y) = xy
n = xy/(x+y)

x(y-n) = yn
x = yn/(y-n)

y = xn/(x-n)


n = 5
(x,y) = (6,30),(10,10)

xn % (x-n) == 0
x-n := z
x = z-n

y = (n+z)n / z
y = n**2 + nz /z
→　n**2 がzで割り切れる
n**2の約数の数に等しい？
→　組み合わせ数は（n**2の約数＋１）//2　に等しい！
→　→　平方数で、約数の数が8*10**6を超えるものを見つければOK

nについて
2**10
3**6
5**4
7**3
11**2
13**2
17**2
19**2

ここまででn**2の約数は
21*13*9*7*5*5*5*5



nはどうせ高度合成数やろ、という決めつけ
nの約数の数は√8＊1000以上 ≒2800ぐらい？

6の約数：４つ
36の約数：9つ
1296の約数：25

n=60
(x,y)
61,61*60
62,62*30
63,63*20
64,64*15
65,65*12
66,66*10
68,34*15
69,23*20
70,420



'''
