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

def main():
    """"ここに今までのコード"""
    import sys
    readline = sys.stdin.readline

    k = int(readline())
    s = readline().strip()
    n = 4**k

    s = s+s
    J = [0] * (2*n+1)
    O = [0] * (2*n+1)
    I = [0] * (2*n+1)
    for i,x in enumerate(s,1):
        J[i] = J[i-1] + (x=='J')
        O[i] = O[i-1] + (x=='O')
        I[i] = I[i-1] + (x=='I')

    pointer = 0
    check = [[] for _ in range(3)]
    for i in range(k-1,-1,-1):
        s_range = 4**(i)
        for j in [0,1,2]:
            check[j].append((pointer,pointer + s_range))
            pointer += s_range

    ans = n
    for i in range(n):
        tmp = 0
        for c_list,sums in zip(check, [J,O,I]):
            for j,k in c_list:
                tmp += sums[k+i] - sums[j+i]

        ans = min(ans,n-tmp)

    print(ans-1)

if __name__ == '__main__':
    main()


'''
方針
ある文字を起点にした時の文字列をSとし、
この時書き換える文字数をxとする。
そこから時計回りに1文字起点をずらすことを考える。

S[4^k+1] がOなら　x+=1、
           Jなら x-=1
S[2*4^k+1] がIなら　x+=1、
            Oなら x-=1
S[3*4^k+1] がJなら　x+=1、
            Iなら x-=1
:
:
S[-3]がOなら　x+=1
       Jなら　x-=1
S[-2]がIなら　x+=1
       Oなら　x-=1
S[-1]がIなら　x-=1
s[0]がO,Iなら　x+=1

1回あたり、３K＋１箇所調べればOK

4^K * (3k+1) ~ 3*10^7なので間に合う？？？

文字列は遅いので、tupleにおきかえます。

'''
