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

import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

n = int(readline())
data = read().split()
x = 10**9

a = []
for si in data:
    if('.' in si):
        num1,num2 = si.split('.')
        a.append(int(num1)*x + int(num2) * 10**(9- len(num2)))
    else:
        a.append(int(si) * x)

fac_25 = [[0]*19 for _ in range(19)]
for ai in a:
    # print(ai)

    num = 2
    cnt2 = 0
    while(ai%num == 0)&(cnt2<18):
        ai //= num
        cnt2 += 1

    num = 5
    cnt5 = 0
    while(ai%num == 0)&(cnt5<18):
        ai //= num
        cnt5 += 1

    fac_25[cnt2][cnt5] += 1

    # print(cnt2,cnt5)

fac_cs = [[0]*19 for _ in range(19)]
for i in range(18,-1,-1):
    for j in range(18,-1,-1):
        fac_cs[i][j] = fac_25[i][j]
for i in range(18,-1,-1):
    for j in range(17,-1,-1):
        fac_cs[i][j] += fac_cs[i][j+1]

for i in range(17,-1,-1):
    for j in range(18,-1,-1):
        fac_cs[i][j] += fac_cs[i+1][j]

ans = 0
for i in range(18,-1,-1):
    for j in range(18,-1,-1):
        ans += fac_25[i][j] * fac_cs[18-i][18-j]

# print(ans)
ans -= fac_cs[9][9]
# print(ans)
ans //=2
print(ans)

# for i in fac_cs:
#     print(i)
#
# print(fac_cs[10][8])
# print(fac_cs[7][10])
# print(fac_cs[9][9])
# print(fac_cs[5][9])


'''
掛け算して、2,5の因子が18個以上あれば整数
'''
