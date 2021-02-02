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

n = 100_000
# n = 29
g_num = [-1] * (n+1)
g_cnt = [0] * (n+1)

squares = []
for i in range(1,400):
    num = i**2
    if(num > n):
        break
    squares.append(num)

ans = 0
g_num[0] = 0
g_cnt[0] += 1
ans += 2

for i in range(1,n+1):
    bit = 0
    for j in squares:
        if(i<j):
            break
        # print(bit,i,j)
        bit = bit | (1 << g_num[i-j])
    cnt = 0
    while(True):
        if((bit >> cnt) & 1):
            cnt += 1
            continue
        g_num[i] = cnt
        g_cnt[cnt] += 1
        break

    if(g_num[i] == 0):
        for j in g_cnt:
            if(j==0):
                break
            ans += j*(j+1)

    else:
        for ind,j in enumerate(g_cnt):
            if(j==0):
                break
            ans += (j * g_cnt[ g_num[i] ^ ind ])
    # print(ans)
    # print(g_num)
    # print(g_cnt)

print(ans//2)
# print(g_num)
# print(g_cnt)





'''
山が一つの時のgrundy数
0,1,2,3,4,5,6,7,8,9,10
0,1,0,1,2,0,1,0,1,2,

grundy数を作って、
xorが0になる組み合わせの数。

cを決めると、
・grundy(c)=0の時
aとbはgrundy数が同じ
a=bがありえる

・grundy(c)=xの時
grundy(a)^grundy(b)= x
必ずa≠b


x*(x-1)//2 + x = x*(x+1)//2

n = 3
(0,0,0)
(0,0,2)
(0,1,1)
0,1,3
偶数の時まけ
0 1
2 2
4 3
6 3
8 1



'''
