import sys
import os
f = open('C:\\Users\\scare\\Documents\\git\\atcoder\\input.txt', 'r')
sys.stdin = f

##############################

import numpy as np
from queue import LifoQueue

#スタックから取り出してもろもろの処理をする関数
# def process_stack(stack, n_search, allows):
#     point = stack.get()
#
#     for direction in ['U', 'L', 'D', 'R']:
#         stack, n_search, allows = direction_search(point, direction, stack, n_search, allows)
#
#     return stack, n_search, allows

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

# robotがゴールに行くまで追いかけ、方向転換があったマスをチェック
def robot_way_check(start, start_direction, goal, allows, turn_check):
    point = start.copy()
    direction = start_direction

    while ( point != goal):
        if( allows[point[0], point[1]] != direction):
            turn_check[point[0], point[1]] = 1
            direction = allows[point[0], point[1]]

        point = neighbor_search(point, direction)

    return( turn_check)


#############################


n, m, b = map(int, input().split())
gy, gx  = map(int, input().split())

ry = np.zeros(m).astype(int)
rx = np.zeros(m).astype(int)
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
    →　「木の中で探索していないノードを一つ選択し」ここを改善する。
    　　何回まっすぐ進めばゴールにたどり着けるか？をコスト情報として持たせれば、案内板を減らせる。
       ゴールを0として、四方の中で最もコストが低いマスの情報で更新していく？

　＜必要なもの＞
　ノード探索表 N*N　状態：｛10000:ブロック　1000:未更新　0:goal　1以上：直進回数（曲がる回数＋１）｝
　ノード追加未探索スタック　：　ノード探索==1のマスを入れておく
　矢印設置結果表 N*N　状態：｛UDRL：上下左右　'0.0'：未設置　B：ブロック｝

2.使わない矢印をはがす
 全ロボットの動きをトレースし、
 方向転換が起きなかったマスは矢印をはがす
 ＜必要なもの＞
 方向転換実施チェック表　N*N


'''

# 方針１
n_search = np.ones([n,n])astype(int) * 1000
n_before_search_s = LifoQueue()
n_before_search_s_next = LifoQueue()
allows = np.zeros([n,n]).astype(str)
# allows = [['N'] * n]  *n

# n_search, allows にブロック情報を入れる
for i in range(b):
    temp_y, temp_x = map(int, input().split())
    n_search[temp_y, temp_x] = 10000
    allows[temp_y, temp_x] = 'B'






#ゴールをqに追加
n_before_search_s.put([gy,gx])

#スタックが空になるまで実行
count = 0
while( n_before_search_s.empty() == False):
    while( n_before_search_s.empty() == False):
        n_before_search_s, n_search, allows = process_stack(n_before_search_s, n_search, allows)



    # next
    count +=1
    n_before_search_s = n_before_search_s_next.copy()
    n_before_search_s_next = LifoQueue()


# 方針2
turn_check = np.zeros([n,n])

for i in range(m):
    #goalに行けないロボットは抜いておく
    if(n_search[ry[i], rx[i]] == 2):
        turn_check = robot_way_check( [ry[i], rx[i]], #start,
                                      c[i], #start_direction,
                                      [gy, gx], #goal,
                                      allows,
                                      turn_check)


for i in range(n):
    for j in range(n):
        if(turn_check[i,j] == 0):
            # print('{} {}'.format(i,j))
            allows[i,j] = '0.0'

#出力
k = np.sum( (allows == 'U') | (allows == 'D') | (allows == 'L') | (allows == 'R' ))
print(k)
for i in range(n):
    for j in range(n):
        temp = allows[i,j]
        if( (temp == 'U') | (temp == 'D') | (temp == 'L') | (temp == 'R' )):
                    print('{} {} {}'.format(i, j, temp) )
