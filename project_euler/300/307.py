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

h = 10**6
k = 20000
# h = 7
# k = 3

p = 0
dp = [[0] * (k+1) for _ in range(2)]
dp[0][0] = 1
for i in range(k//2 + 1):
    # print(i)
    # print(dp)
    if(i%500==0):
        print(i)
    i2 = i%2
    for j in range(k+1):
        if(i*2+j > k):
            break

        if(i==0)&(j==0):
            continue

        if(i==0):
            dp[i2][j] = dp[i2][j-1] * (h-i-j+1)/h
        elif(j==k):
            dp[i2][j] = dp[i2][j-1] * (h-i-j+1)/h
        else:
            dp[i2][j] = dp[i2][j-1] * (h-i-j+1)/h + dp[1-i2][j+1] * (j+1)/h

    p += dp[i2][k-i*2]


print(p)
print(1-p)



        # if(i==k//2)&(j==k):
        #     continue
        # if(i==k//2):
        #     dp[1-i2][j+1] += dp[i2][j] * (h-i-j)
        # elif(j==k):
        #     dp[1-i2][j-1] += dp[i2][j] * j
        # elif(j==0):
        #     dp[i2][j+1] += dp[i2][j] * (h-i-j)
        # else:
        #     dp[i2][j+1] += dp[i2][j] * (h-i-j)
        #     dp[1-i2][j-1] += dp[i2][j] * j

# p = 0
# for i in range(10001):
#     p += dp[i][20000-2*i]
#
# print(p)
# print(1-p)

'''
10**6個作ったときに、3か所以上の欠陥があるチップが1つ以上発生する確率を問われています。
(1*20000,0*980000)
(2*1,1*19998,0*980001)
(2*2,1*19996,0*980002)
:

(2*x,1*20000-2x,0*980000+x)

これを足していけばOKだが・・・



ボール1個の人数、2個の人数 = (b1,b2,over)
として、
最初(0,0)=1 から20000かいボールを配るとする。

(h-b1-b2-over)/hの確率でb1が1増える
b1/hの確率でb1が減ってb2が増える
b2/hの確率でb2が減ってoverが増える

だけども、overは0だけ計算して、最後に足せばよい？

パターンが多い・・・
いや、10**8でいけるか？

'''

#
#
#
#
#
# from decimal import *
#
# # h = 10**6
# # b = 2*10**4
# h = Decimal(1000000.0000000000)
# b = Decimal(20000.0000000000)
# one = Decimal(1.0000000000)
# two = Decimal(2.0000000000)
#
# # p_ = ((h-1)/h)**19998 * (((h-1)/h)**2 + ((h-1)/h)*(20000/h) + 10000*19999/h**2)
# p_ = (((h-one)/h)**(b-two)) * ((h-one)**two + (h-one)*b + (b*(b-one))/two )/(h**two)
# print(p_)
# print(one-p_)
#
# # print((((h-1)/h)**2 + ((h-1)/h)*(20000/h) + 10000*19999/h**2))
#
# h = Decimal(7.0000000000)
# b = Decimal(3.0000000000)
# one = Decimal(1.0000000000)
# two = Decimal(2.0000000000)
#
# # p_ = ((h-1)/h)**19998 * (((h-1)/h)**2 + ((h-1)/h)*(20000/h) + 10000*19999/h**2)
# p_ = (((h-one)/h)**(b-two)) * ((h-one)**two + (h-one)*b + (b*(b-one))/two )/(h**two)
# print(p_)
# print(one-p_)
#
# print((one/h)**3)
#
# '''
# 20000個のボールを1000000人に無作為に分けるとき、
# ある人が3個以上ボールをもらえる確率。
# つまり、0個でも1個でも2個でもない確率。
# 10*6 = hとして
# 0個　→　((h-1)/h)**20000
# 1個　→　((h-1)/h)**19999 * 1/h * 20000C1
# 2個　→　((h-1)/h)**19998 * (1/h)**2 * 20000C2
#
# 足すと、
# ((h-1)/h)**19998 * ((h-1)/h)**2 + (h-1)/h)*(20000/h) + 10000*19999/h)
#
# 精度怖いけど計算してみましょう。
#
# ==========
# 違うみたいですね。
#
# p0 =　欠陥0個のチップができる確率
# p1 =　欠陥1個のチップができる確率
# p2 =　欠陥2個のチップができる確率
# ：
#
# とする。
# Σpi = 1
# Σi*Pi = k/n
# p0 = (n-k)/n
# (1-p0)/p0 = (1-p0-p1)/p1
#
# k,n = 3,7のとき
# # p0 = 4/7
# # p1 = 12/49
# # p2 = 36/343
# p0 = 7/10
# p1 =
#
#
# '''
#
# print(1- 4/7 - 12/49 - 36/343)
# print(20/98)
