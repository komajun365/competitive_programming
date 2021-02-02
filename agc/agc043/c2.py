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

def main():
    """"ここに今までのコード"""
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines

    n = int(readline())
    data = tuple(map(int,read().split()))
    m1 = data[0]
    ab = data[1:1+2*m1]
    m2 = data[1+2*m1]
    cd = data[2+2*m1:2+2*(m1+m2)]
    m3 = data[2+2*(m1+m2)]
    ef = data[3+2*(m1+m2):]

    mod = 998244353
    mods = [1] * (n+10)
    base = pow(10,18,mod)
    for i in range(1,n+1):
        mods[i] = (mods[i-1] * base)%mod

    def calc_node(xy):
        links = [[] for _ in range(n+1)]
        it = iter(xy)
        for x,y in zip(it,it):
            if(x < y):
                x,y = y,x
            links[y].append(x)

        group = [-1] * (n+1)
        g_bit = [0] * (n+1)
        group[-1] = 0
        g_bit[-1] = 1
        num_max = 1
        for i in range(n,0,-1):
            tmp = 0
            for j in links[i]:
                tmp |= g_bit[j]
            cnt = 0
            while(tmp&1):
                tmp = tmp>>1
                cnt+=1
            group[i] = cnt
            g_bit[i] = 1 << cnt
            num_max = max(num_max,cnt)

        res = [0] * (num_max+1)
        for i,num in enumerate(group[1:],1):
            res[num] += mods[i]
            res[num] %= mod

        return res

    x = calc_node(ab)
    y = calc_node(cd)
    z = calc_node(ef)

    if(len(x) < len(y)):
        x,y = y,x
    if(len(y) < len(z)):
        y,z = z,y
    if(len(x) < len(y)):
        x,y = y,x


    len_2 = 2**(len(y)-1).bit_length()
    yz = [0] * (len_2)
    for j in range(len(y)):
        for k in range(len(z)):
            yz[j^k] += y[j]*z[k]
            yz[j^k] %= mod

    ans = 0
    for i,j in zip(x,yz):
        ans += i*j
        ans %= mod

    print(ans)

if __name__ == '__main__':
    main()



#
# ans = 0
# for i in range(cyc):
#     tmp = 1
#     for w in [x,y,z]:
#         num = 0
#         for j in w[i]:
#             num += mods[j]
#             num %= mod
#         tmp *= num
#         tmp %= mod
#     ans += tmp
#
# ans %= mod
# print(ans)
#
# print(xg)

'''
方針
重みの条件から、i+j+kの大きいものから貪欲にとっていけばいいことがわかる。
また、i+j+kの合計が同じ頂点同士には辺を作らない。



まずはグラフXについて、
頂点Nを採用し、Nとつながっている頂点をすべて捨てる。
その後、残っている頂点の中で最大のものを採用し、つながっている頂点をすべて捨てる
。。。を繰り返して、残ったものがXiの中で独立集合として採用できる。
グラフY,Zについても同様に考えることができる。

残った頂点の集合を
A=(Xa1,Xa2,...Xaj)
B=(Yb1,Yb2,...Ybk)
C=(Zc1,Zc2,...Zcl)
とすれば、求めたいものはΣ(10^18(a+b+c))となる。

式展開すると
=Σ((10^18a)*(10^18b)*(10^18c))
=Σ((10^18a)*(10^18b)) * Σ(10^18c)
=Σ(10^18a) * Σ(10^18b) * Σ(10^18c)
で求められる。

'''
