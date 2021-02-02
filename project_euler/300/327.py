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

c_max = 40
r_max = 30

mcr = [[-1] * (r_max+1) for _ in range(c_max+1)]
def calc(c,r):
    # print(c,r)
    if(mcr[c][r] != -1):
        return mcr[c][r]
    if(c-r>=1):
        mcr[c][r] = r+1
        return mcr[c][r]

    bef = calc(c,r-1)
    once = c-2
    for j in range(c-1,-1,-1):
        if((bef-j)%once==0):
            i = (bef-j)//once
            break

    mcr[c][r] = i*c + j+1
    return mcr[c][r]

print(calc(3,6))
print(calc(4,6))

ans = 0
for c in range(3,c_max+1):
    print(c)
    ans += calc(c,r_max)

print(ans)

'''
M(x,x-1) = x
M(x,x+1) は、
1の部屋に入った後でx枚のカードを持っている状態を作ることと考えると、
1の部屋に1枚カードを置いて戻ってくる必要がある。
ので、M(x,x+1) = M(x,x)+3

M(C,？)のとき、
x枚のカードが使えるとして、どこまでいけるか、を考える。
C枚のカードを使うと、C-2枚のカードを次の部屋に持っていける。
x = ic+jとすると、
i(c-2)+j-1枚を持った状態で次の部屋sに行ける。

M(4,6)= 23 = 5*4+3
M(4,5) =  12 = 2*4 + 4
M(4,4) = 7 = 1*4 + 3
M(4,3) = 4

逆算したい。
M(4,3) = 4 = 1*(4-2) + 2
M(4,4) = 1*4 + 2 + 1


M(3,2) = 3 = 1*(3-2) + (3-1)
M(3,3) = 6 = 4*(3-2) + (3-1)
M(3,4) = 15 = 13*(3-2) + (3-1)
M(3,5) = 42 = 40*(3-2) + (3-1)

'''
