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

n,l = map(int,input().split())
s = [input() for _ in range(n)]
s2 = [(len(si),si) for si in s]
s2.sort()

max_d = s2[-1][0]
cnt = [0] * (max_d+1)
stack = set()
down = 0
for i in range(max_d,-1,-1):
    now = 0
    next = set()
    while(stack):
        sj = stack.pop()
        next.add(sj//2)
        now += 1

    cnt[max_d-i] = now*2 - down

    if(s2):
        while(s2[-1][0] == i):
            _,sj = s2.pop()
            if(len(sj)>0):
                next.add(int(sj,2)//2)
                now += 1
            if(len(s2)==0):
                break
    down = now
    stack = stack.union(next)

num = 0
for i,ci in enumerate(cnt[1:]):
    num += 2**i * (ci%2)

# def calc(x):
#     if(x==0):
#         return 0
#     elif(x==1):
#         return 1
#     y = x.bit_length()//2
#     block = 4**y //2
#     if( x//block in [1,3]):
#         return 1
#     else:
#         return 1-calc(x - block*2)

if(calc(num)==0):
    print('Bob')
else:
    print('Alice')





'''
二部木で考えて、
先祖と子孫を消していくゲーム

何かを消したとき、常に残りは二部木の森になっている？

深さxの木に対する操作結果
・全消し
・深さx-1の木を残す
・深さx-1,x-2の木を残す
・深さx-1,...,x-iの木を残す
・深さx-1,...,1の木を残す

下から見ていって、
奇数なら先手の勝ち、偶数なら後手の勝ち。

が先手勝ちの状態で、次の桁が奇数なら

topが奇数なら先手の勝ち。
偶数なら、それより下の状態が先手勝利なら先手、それ以外は後手。

全部偶数のパターンだけ後手が勝てる、それ以外は負け？

初期状態の把握



'''
