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

from collections import defaultdict

s = input()

n = len(s)
inf = 10**6
d = defaultdict(lambda : inf)
d[0] = 0

a = ord('a')
now = 0
for i in range(n):
    si = ord(s[i]) - a
    now = now^(1<<si)
    for j in range(26):
        d[now] = min(d[now], 1+d[now^(1<<j)])

print(max(1,d[now]))


'''
[a,b,c,...,z]を、
偶数のみ　or　奇数1個だけ　に分割できれば良い


s[i,j]が上記条件を満たしているか、高速に判定できる？
→　a-zまでの累積を持っていればO(26)で計算できる

calc(0,n) = max( calc(0,i) + calac(i,n) )

どう頑張ってもcalc(0,n) = nになるような文字列は？


abcdeabca
00000
10000
11000
11100
11110
11111
01111
00111
00011
10011
10001
11000

状態は2**26に圧縮できる。
≒6.7*10**7　大きい。。。

けど、実際はそんなにチェックしなくていいのか？
defaultdictで遷移できる27個を探して、一番少なく飛んでこれる数にすればよい。

abcbaee

abcabcxabcx
0000:0
1000:1
1100:2
1110:3
0110:4
0010:5
0000:0
0001:1
1001:2
1101:3
1111:4
1110:3

以前と同じ状態に戻ってきたら、同じで良い。OK。

'''
