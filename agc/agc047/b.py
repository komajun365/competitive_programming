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
s = read().split()
s.sort(key= lambda x: len(x))

words = dict()
# for si in 'abcdefghijklmnopqrstuvmxyz':
#     words[si] = dict()

ans = 0
for si in s:
    if(len(si)==1):
        head = si[0]
        tail = ''
    else:
        head = si[0]
        tail = si[1:]

    heads = set()
    heads.add(head)
    stack = ['']
    now = ''
    for ti in tail[::-1]:
        now += ti
        stack.append(now)

    for i,tmp in enumerate(stack):
        if( tmp in words):
            for j in heads:
                if(j in words[tmp]):
                    ans += words[tmp][j]
        if(i==len(tail)):
            break
        heads.add(tail[i])

    if(not tail in words):
        words[tail] = dict()
    if(not head in words[tail]):
        words[tail][head] = 1
    else:
        words[tail][head] += 1

print(ans)
#
for k,v in words.items():
    print(k)
    print(v)
