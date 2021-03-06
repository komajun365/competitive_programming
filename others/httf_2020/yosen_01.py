import sys
import os
f = open('C:\\Users\\scare\\Documents\\git\\atcoder\\input.txt', 'r')
sys.stdin = f

##############################

import numpy as np
from queue import LifoQueue

#スタックから取り出してもろもろの処理をする関数
def process_stack(stack, n_search, allows):
    point = stack.get()

    for direction in ['U', 'L', 'D', 'R']:
        stack, n_search, allows = direction_search(point, direction, stack, n_search, allows)

    return stack, n_search, allows


#direction側の見て、そこのpointを返す
def neighbor_search(point, direction):
    if(direction == 'U'):
        next_point = [ (point[0] -1)%n , point[1]]
    elif(direction == 'D'):
        next_point = [ (point[0] +1)%n , point[1]]
    elif(direction == 'L'):
        next_point = [ point[0] , (point[1] -1)%n ]
    elif(direction == 'R'):
        next_point = [ point[0] , (point[1] +1)%n ]

    return(next_point)

# 1方向のサーチと書き換えを行う
def direction_search(point, direction, stack, n_search, allows):
    n_search[point[0], point[1]] = 2

    next_point = neighbor_search(point, direction)
    rev_direction = {'U':'D',
                     'D':'U',
                     'R':'L',
                     'L':'R',
                      }

    while( n_search[next_point[0], next_point[1]] ==  0):
        stack.put(next_point)
        n_search[next_point[0], next_point[1]] = 1
        allows[next_point[0], next_point[1]] = rev_direction[direction]

        next_point = neighbor_search(point, direction)

    return stack, n_search, allows



#############################


n, m, b = map(int, input().split())
gy, gx  = map(int, input().split())

ry = np.zeros(m)
rx = np.zeros(m)
c = [0] * m

for i in range(m):
 temp = input().split()
 ry[i] = int(temp[0])
 rx[i] = int(temp[1])
 c[i] = temp[2]

by = np.zeros(b)
bx = np.zeros(b)

# for i in range(b):
#     by[i], bx[i] = map(int, input().split())

# ここまでinput
'''
方針を考える
1.ゴールマスを木の根とする。
　以下を「探索していないノード」がなくなるまで繰り返す。
　木の中で探索していないノードを一つ選択し、周囲4方向の直線状にあるマスを自分の子にする。
　ただし、ブロックマスや、すでに誰かの子になっているマスは自分の子にせず、
　それより奥にあるマスも自分の子にはしない。
　子になったノードには、自分の親の方向を向く矢印を設定する。
　＜必要なもの＞
　木：　いらないのでは？
　ノード探索表 N*N　状態：｛0:ノード未追加　1:ノード追加未探索　2:ノード追加探索済｝
　ノード追加未探索スタック　：　ノード探索表==1のマスを入れておく
　矢印設置結果表 N*N　状態：｛UDRL：上下左右　'0.0'：未設置　B：ブロック｝

2.使わない矢印をはがす
 全ロボットの動きをトレースし、
 方向転換が起きなかったマスは矢印をはがす

'''

# 方針１
n_search = np.zeros([n,n])
n_before_search_s = LifoQueue()
allows = np.zeros([n,n]).astype(str)
# allows = [['N'] * n]  *n

# n_search, allows にブロック情報を入れる
for i in range(b):
    temp_y, temp_x = map(int, input().split())
    n_search[temp_y, temp_x] = 2
    allows[temp_y, temp_x] = 'B'


#ゴールをqに追加
n_before_search_s.put([gy,gx])

#スタックが空になるまで実行
while( n_before_search_s.empty() == False):
    n_before_search_s, n_search, allows = process_stack(n_before_search_s, n_search, allows)

#出力
k = np.sum( (allows == 'U') | (allows == 'D') | (allows == 'L') | (allows == 'R' ))
print(k)
for i in range(n):
    for j in range(n):
        temp = allows[i,j]
        if( (temp == 'U') | (temp == 'D') | (temp == 'L') | (temp == 'R' )):
                    print('{} {} {}'.format(i, j, temp) )


##############################

#スタックから取り出してもろもろの処理をする関数
def process_stack(stack, n_search, allows):
    point = stack.get()

    for direction in ['U', 'L', 'D', 'R']:
        stack, n_search, allows = direction_search(point, direction, stack, n_search, allows)

    return stack, n_search, allows


#direction側の見て、そこのpointを返す
def neighbor_search(point, direction):
    if(direction == 'U'):
        next_point = [ (point[0] -1)%n , point[1]]
    elif(direction == 'D'):
        next_point = [ (point[0] +1)%n , point[1]]
    elif(direction == 'L'):
        next_point = [ point[0] , (point[1] -1)%n ]
    elif(direction == 'R'):
        next_point = [ point[0] , (point[1] +1)%n ]

    return(next_point)

# 1方向のサーチと書き換えを行う
def direction_search(point, direction, stack, n_search, allows):
    n_search[point[0], point[1]] = 2

    next_point = neighbor_search(point, direction)
    rev_direction = {'U':'D',
                     'D':'U',
                     'R':'L',
                     'L':'R',
                      }

    while( n_search[next_point[0], next_point[1]] ==  0):
        stack.put(next_point)
        n_search[next_point[0], next_point[1]] = 1
        allows[next_point[0], next_point[1]] = rev_direction[direction]

        next_point = neighbor_search(point, direction)

    return stack, n_search, allows
