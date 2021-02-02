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
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m = map(int, readline())
uvs = list(map(int,read().split()))

links = [dict() for _ in range(n+1)]
it = iter(uvs)
for u,v,s in zip(it,it,it):
    links[u][v] = s
    links[v][u] = s

def not_bigraph(start,parent2,parent):
    loop = [start]
    i = start
    while(parent[i] != -1):
        i = parent[i]
        loop.append(i)
    loop2 = [parent2]
    i = parent2
    while(parent[i] != -1):
        i = parent[i]
        loop2.append(i)

    while(loop[-2] == loop2[-2]):
        loop.pop()
        loop2.pop()

    loop = loop[:-1] + loop2[::-1] + [start]
    ln = len(loop)
    s_odd = 0
    s_even = 0
    for ind in range(ln-1):
        i,j = loop[ind:ind+2]
        if(ind%2==0):
            s_even += links[i][j]
        else:
            s_odd += links[i][j]

    if(s_even <= s_odd)|((s_even-s_odd)%2==1):
        return 0

    nums = [-1] * (n+1)
    nums[start] = (s_even-s_odd)//2

    parent = [-1] * (n+1)
    stack = [start]
    while(stack):
        next = []
        while(stack):
            i = stack.pop()
            for j,s_ij in links[i].items():
                if(j == parent[i]):
                    continue
                num_j = s_ij - nums[i]
                if(num_j <= 0):
                    return 0
                if(nums[j] == -1):
                    nums[j] = num_j
                    parent[j] = i
                    next.append(j)
                else:
                    if(nums[j] != num_j):
                        return 0
        stack = next[::]

    return 1



#二部グラフ判定
root = 1
parent = [-1] * (n+1)
bigraph = [-1] * (n+1)
bigraph[root] = 0
nums = [0] * (n+1)
stack = [root]
color = 1
while(stack):
    next = []
    while(stack):
        i = stack.pop()
        for j,s_ij in links[i].items():
            if(j == parent[i]):
                continue
            if(bigraph[j] == -1):
                bigraph[j] = color
                parent[j] = i
                next.append(j)
            else:
                if(bigraph[j] != color):
                    #二部グラフじゃなかった場合
                    print(not_bigraph(j,i,parent))
                    exit()
    stack = next[::]
    color = 1-color

#二部グラフだった場合
inf = -1 * 10**15
nums = [inf] * (n+1)




'''
ある頂点の値を決めると、
他の頂点の値は全て決まる？

ループがなければこれで上下限を求めていけそう。
ループがある場合は？


ある頂点の値がi,j(i<j)で書き込み可能な時
i<x<jを満たすxはいけるのでは？

二分探索チックにいけないかしら？

ある頂点の値を1増やすと、
距離偶数の頂点は1増える
距離奇数の頂点は１減る

ループがあって、偶数かつ奇数な距離のある頂点が発生すると、解は高々1通り。
→　奇数長のループをみつけて、ループの解を決めてしまう。
　そこからすべての頂点に矛盾なく割り当てできれば1

そうでない場合、二部グラフ。
どちらかの部集合を増やす、減らす、で新しい組み合わせが作れる。

'''
