# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

import sys
read = sys.stdin.buffer.read

n,m,*xy = map(int,read().split())

links = [[] for _ in range(n)]
for i in range(m):
    x,y = xy[2*i:2*i+2]
    x -= 1
    y -= 1
    links[x].append([y,i])
    links[y].append([x,i])

def calc(root):
    res = [[0,m] for _ in range(n)]
    res[root][0] = m
    depth = [-1] * n
    depth[root] = 0
    stack = [root]
    while(stack):
        stack2 = []
        while(stack):
            i = stack.pop()
            for j,num in links[i]:
                if depth[j] > depth[i]:
                    continue

                if res[i][1] == num or res[j][1] == num
                    continue
                if res[i][1] < num and res[j][1] < num:
                    continue
                elif res[i][1] > num and res[j][1] < num:
                    if res[i][0] > num:
                        res[root] = [0,0]
                        return res
                    res[i][1] = num
                elif res[i][1] < num and res[j][1] > num:
                    if res[j][0] > num:
                        res[root] = [0,0]
                        return res
                    res[j][1] = num
                else:
                    if res[i][0] == res[i][1] and res[j][0] <= num:
                        res[j][0] = num
                        res[j][1] = num
                    elif res[j][0] == res[j][1] and res[i][0] <= num:
                        res[i][0] = num
                        res[i][1] = num
                    else:





'''
0,1,2
-> [3,0,1,2]

0,2,1
->[[3,3],[0,0],[0,1],[0,3]] #ここまでは生きていないとダメ　-　遅くともここで死ぬ

1,2,0
->[[3,3],[1,1],[0,0],[0,3]]

1,2,0,3
->[[4,4],[1,1],[0,0],[0,4],[0,4]]


'''


