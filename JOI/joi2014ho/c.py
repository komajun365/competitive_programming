# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# 検討24分　実装12分 バグとり0分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
import bisect

n = int(readline())
a = tuple(map(int,read().split()))

s = [0] *(2*n+1)
for i in range(2*n):
    s[i+1] = s[i] + a[i%n]

ans = 0
i = 0
j = 1
while(i<n):
    sa = s[j]-s[i]
    k = bisect.bisect_left(s, sa + s[j])
    sb = s[k] - s[j]
    sc = s[i+n] - s[k]
    if(sa <= sb)&(sa <= sc):
        ans = max(ans, sa)
        j += 1
    else:
        i += 1
        if(i==j):
            j += 1

print(ans)

'''
方針
尺取りしながら二分探索。
A1・・・AnA1・・・Anで累積和を作っておく。
（S1・・・S2n）とする

JOI君が時計回りに[Ai~A(j-1)]の領域を食べたいとする。
するとピースの大きさは、sa = S(j)-S(i)。
sb = S(k)-S(j)
sc = S(i+n)-S(k)
sa <= sb, sa <= sc
となるようにうまくkを設定できれば勝ち。
 k= bisect.bisect_left(s, sa+S(j) )で判定できる。

kがOKならｊをインクリメント、
ｋがNGならiをインクリメントし、
i=nになるまで進めればOK.
計算量はO(NlogN)
'''
