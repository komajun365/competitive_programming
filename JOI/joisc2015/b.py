# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討13分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

k = int(input())
s = input()
n = 4**k

ans = 0
pointer = 0
check = [[] for _ in range(3)]
for i in range(k-1,-1,-1):
    s_range = 4**(i)
    for j,x in enumerate('JOI'):
        ans += s_range - s.count(x, pointer, pointer + s_range)
        pointer += s_range
        if(i==0)&(j==2):
            break
        check[j].append(pointer)

now = ans
for i in range(n-1):
    for c_list,good,bad in zip(check, 'JOI', 'OIJ' ):
        for j in c_list:
            if(s[(j+i)%n] == good):
                now -= 1
            elif(s[(j+i)%n] == bad):
                now += 1
    if(s[i] != 'J'):
        now -= 1
    if(s[i-1] != 'I'):
        now += 1

    ans = min(ans,now)

print(ans)





'''
方針
ある文字を起点にした時の文字列をSとし、
この時書き換える文字数をxとする。
そこから時計回りに1文字起点をずらすことを考える。

S[4^k] がOなら　x+=1、
           Jなら x-=1
S[2*4^k] がIなら　x+=1、
            Oなら x-=1
S[3*4^k] がJなら　x+=1、
            Iなら x-=1
:
:
S[-3]がOなら　x+=1
       Jなら　x-=1
S[-2]がIなら　x+=1
       Oなら　x-=1
S[-1]がIじゃないなら　x+=1
s[0]がJじゃないなら　x-=1

これを4^k回繰り返す。
1回あたり、３K＋１箇所調べればOK

4^K * (3k+1) ~ 3*10^7なので間に合う？？？
pypyだとぎりぎりのような気がする。。。
'''
