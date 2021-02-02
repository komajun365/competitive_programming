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

b = [input() for _ in range(19)]

black = set()
white = set()
for i in range(19):
    for j in range(19):
        if(b[i][j] == 'o'):
            black.add(i*19+j)
        elif(b[i][j] == 'x'):
            white.add(i*19+j)

def check(stones):
    for i in range(19):
        for j in range(19):
            for dx,dy in [[1,0],[0,1],[1,1],[-1,1]]:
                for k in range(5):
                    ii = i + dx*k
                    jj = j + dy*k
                    if(ii<0)|(ii>=19)|(jj<0)|(jj>=19):
                        break
                    if(not ii*19+jj in stones):
                        break
                else:
                    return True
    return False

b_num = len(black)
w_num = len(white)
if(b_num<w_num)|(b_num-w_num>1):
    print('NO')
    exit()

b_win = check(black)
w_win = check(white)
if(b_win)&(w_win):
    print('NO')
    exit()

if(b_win)&(b_num-w_num==0):
    print('NO')
    exit()

if(w_win)&(b_num-w_num==1):
    print('NO')
    exit()

if(not b_win)&(not w_win):
    print('YES')
    exit()

if(b_win):
    stones = black
else:
    stones = white

st_list = list(stones)

for rem in st_list:
    stones.remove(rem)

    if(not check(stones)):
        print('YES')
        exit()

    stones.add(rem)

print('NO')

'''
方針
・碁石の数を数える

・終了条件チェッカーを作る
終了状態の場合、
両方が勝っていないことを確認。

黒が勝ったなら黒が1多い
白が勝ったなら黒白同数であることを確認

その後、勝った方の碁石を1個づつ取り除き、
いづれかのケースで勝利条件を満たしていないことを確認。

・終了条件チェッカーの計算量
たて：19*19*5
よこ：19*19*5
ななめ：19*19*5*2

だいたい20*20*5*4 = 8000
よゆうですね

'''
