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

    s2 = [0]*n
    for i,x in enumerate(s):
        if(x=='O'):
            s2[i]=1
        elif(x=='I'):
            s2[i]=2
    s2 = tuple(s2)

    ans = 0
    pointer = 0
    check = [[] for _ in range(3)]
    for i in range(k-1,-1,-1):
        s_range = 4**(i)
        for j in [0,1,2]:
            ans += s_range - s2[pointer:pointer + s_range].count(j)
            pointer += s_range
            if(i==0)&(j==2):
                break
            check[j].append(pointer)

    now = ans
    for i in range(n-1):
        for c_list,good,bad in zip(check, [0,1,2], [1,2,0]):
            for j in c_list:
                tmp = s2[(j+i)%n]
                now -= (tmp == good)
                now += (tmp == bad)
        now -= (s2[i] != 0)
        now += (s2[i-1] != 2)

        ans = min(ans,now)

    print(ans)


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
