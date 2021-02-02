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

ans = 0
stack = [(1,3)]
for i in range(26):
    print(i,len(stack))
    stack2 = []
    while(stack):
        j,done = stack.pop()
        for k in range(2):
            next = j*2 + k
            n_done = next&31
            if((done>>n_done) & 1):
                continue
            stack2.append((next, done|(1<<n_done)))

    stack = stack2[::]

# print(stack)
for j,done in stack:
    for i in range(4):
        j = j*2
        n_done = j&31
        if((done>>n_done) & 1):
            break
        done = done|(1<<n_done)
    else:
        ans += j

print(ans>>4)

'''
dfsしましょう

'''
