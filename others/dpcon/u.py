import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

n_bit = 2**n

# １の立つ数で仕分けしておく
flag_num = {}
log2_num = {}
for i in range(n+1):
    flag_num[i] = []
    log2_num[2**i] = i

for i in range(n_bit):
    num = str(bin(i)).count('1')
    flag_num[num].append(i)

#bit演算
# https://www.slideshare.net/KMC_JP/slide-www

# いくつかのウサギを同じグループにした時の点数を計算しておく
g = [0]*n_bit
for i in range(2,n+1):
    for j in flag_num[i]:
        #1になっている一番下の桁の取得
        left_flag = j & (-j)
        #一番左の1だけ反転
        right_flags = j - left_flag

        g[j] = g[right_flags]
        left = log2_num[left_flag]
        for k in range(n+1):
            if( ((right_flags >> k) & 1)  > 0):
                g[j] += a[left][k]

#dpを更新する
init = -1 * 150 * 10**10
dp = [init] * n_bit
dp[0] = 0
for i in range(1,n+1):
    for j in flag_num[i]:
        temp = init
        k = (j-1) & j
        while( k >= 0):
            ### ここに処理を描く ###
            temp = max(temp, dp[k] + g[j-k] )

            # k==0ならbreak
            if(k==0):
                break
            #kの更新
            k = (k-1) & j
        dp[j] = temp

print(dp[n_bit - 1])
