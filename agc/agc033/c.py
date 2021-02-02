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

n = int(readline())
ab = list(map(int,read().split()))

links = [[] for _ in range(n+1)]
it = iter(ab)
for a,b in zip(it,it):
    links[a].append(b)
    links[b].append(a)

def bfs(root):
    depth = [-1] * (n+1)
    depth[root] = 0
    stack = [root]
    for i in range(1,n+1):
        next = []
        if(len(stack)==0):
            break
        while(stack):
            parent = stack.pop()
            for j in links[parent]:
                if(depth[j] == -1):
                    depth[j] = i
                    next.append(j)
        stack = next[::]

    return depth,parent

depth,root2 = bfs(1)
depth,root2 = bfs(root2)
r = max(depth)

if(r%3==1):
    print('Second')
else:
    print('First')


'''
毎回、葉が消える。
ただし、選んだ頂点vが葉であれば、それは生き残る。

つまり、すべての葉を消すor一つ以外の葉を消す、のいずれかの処理をしていくことになる。

全ての葉が消える　→　グラフの直径が２減る
うまく葉を選ぶ　→　グラフの直径が1減る

グラフの直径を1にすれば勝ち？
それまでは2択を絶対に選べる？→選べる

というわけで、直径の長さrを求めて、
r%3 == 1 なら後攻の勝ち
それ以外は先攻の勝ち

木の直径を求めるには、二回BFSすればOK

'''
