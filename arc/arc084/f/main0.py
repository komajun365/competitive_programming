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

n,x = input().split()
n = int(n)
x = int(x, 2)
lx = len(bin(x))-2

a = [int(input(), 2) for _ in range(n)]
a.sort()
la = [len(bin(ai))-2 for ai in a]
mod = 998244353

l = 4000
base = [0] * (l+10)

def add(z,lz):
    for i in range(lz,-1,-1):
        if z < (1 << i):
            continue
        if base[i] == 0:
            base[i] = z
            i += 1
            while i < lz:
                if base[i] == 0:
                    base[i] = base[i-1] * 2
                    i += 1
                else:
                    break
            return
        z = min(z, z^base[i])

idx = 0
for i in range(l):
    base[i] = base[i-1] * 2
    while idx < n:
        if la[idx] == i+1:
            add(a[idx], i)
            idx += 1
        else:
            break
    if i < 20:
        print(base[:20])

cnt = [0] * (l+10)
for i in range(l):
    cnt[i] = cnt[i-1] + (base[i] != 0)

ans = 0
x2 = x
now = 0
for i in range(lx-1,-1,-1):
    if base[i] == 0:
        if now <= x2:
            ans += 1
            ans %= mod
        break
    if x2 >= (1<<i):
        ans += pow(2,cnt[i-1],mod)
        ans %= mod
        x2 ^= (1<<i)
        if now < (1<<i):
            now ^= base[i]
        now ^= (1<<i)
    elif now >= (1<<i):
        now ^= base[i]
    # print(ans,now, cnt[i-1], i)
else:
    ans += 1
    ans %= mod

print(ans)

# print(base[:10])

# for i in range(15):
#     print(base[i])



# print(la)


'''
14
[0,0,6,12]

12 no use
-> 0,6

12 = b1100
14^12 = 2 = b10

6 use
12^6 = b1010
-> 10

2^14 = 12

=====

x,now = 1,1のとき
baseつかえば残りはOK

x,now = 1,0のとき
baseつかわなければ残りはOK


x,now = 0,1のとき
baseつかわなきゃアウト
使ったとて残りがOKかは不明

x,now = 0,0のとき
baseつかったらアウト
使わなかったとて残りがOKかは不明

=========

4 111001100101001
   10111110 : 190
  100000101
 1001000110
11110000011

  101111100
  100000101
    1111001 : 121

 1000001010
 1001000110
    1000110 : 70

    1000110
    1111001
     111111 : 31

==
 1011111000
 1001000110
   10111110 : 


'''