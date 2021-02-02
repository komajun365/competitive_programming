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
parent = set()
child = dict()
for _ in range(n):
    large,m,small = readline().split()
    m = int(m)

    if(large in parent):
        child[large][small] = m
    else:
        parent.add(large)
        child[large] = dict()
        child[large][small] = m

ans = ['hoge',0,'hoge']
for i in parent:
    stack = [(1,i)]
    done = set()
    done.add(i)
    while(stack):
        print(stack)
        num_j, j = stack.pop()
        if(not j in child):
            if( num_j > ans[1]):
                ans = [i,num_j,j]
                print(ans)
            continue
        for k,val in child[j].items():
            if(k in done):
                continue
            stack.append((num_j*val,k))
            done.add(k)

print('1{}={}{}'.format(*ans))
