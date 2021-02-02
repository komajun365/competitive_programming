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


n = int(input())
n_len = n.bit_length()
ans = ['Takahashi','Aoki']

if(n_len==1):
    print(ans[1])
    exit()

num = 0
if(n_len%2==1):
    num = 1

for i in range(n_len//2):
    num = num*4 + 2

print(ans[(n<num)^(n_len%2)])
# print(n_len,num)

'''
数xが2進数でy桁の時、
頭から1桁目は1
それ以外の頭から偶数桁目は高橋君が
奇数桁目は青木君が決められる。

・nが奇数桁
→　高橋君はなるべく数を大きく、青木君はなるべく数を小さくする。
　最後に青木君が数字を決めたときに超えたら高橋君の勝ち

・nが偶数桁
→　高橋君はなるべく数を小さく、青木君はなるべく数を大きくする。
　最後に高橋君が数字を決めたときに超えたら高橋君の勝ち


(n>=num , n_len==偶数)：高橋君win
(n<num , n_len==偶数)：高橋君win



'''
