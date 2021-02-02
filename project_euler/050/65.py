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

'''
pythonなので愚直計算でいけますね
'''

e_mat = [2]
for i in range(1,34):
    e_mat.append(1)
    e_mat.append(i*2)
    e_mat.append(1)

chi,mat = 1,1
for i in e_mat[:-1][::-1]:
    chi,mat = mat,chi+mat*i

# print(e_mat)
# print(chi)
# print(mat)

ans = 0
while(mat>0):
    ans += mat%10
    mat //= 10

print(ans)
