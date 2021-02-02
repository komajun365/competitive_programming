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

    now = ''
    stack = ['']
    for ti in tail[::-1]:
        now += ti
        stack.append(now)

    for ti in stack[::-1]:
        if(ti in words):
            for j in heads:
                if(j in words[ti]):
                    ans += words[ti][j]
        if(ti==''):
            break
        heads.add(ti[-1])

    tail = stack[-1]

    if(not tail in words):
        words[tail] = dict()
    if(not head in words[tail]):
        words[tail][head] = 1
    else:
        words[tail][head] += 1

    # print(si,ans)
    # print(stack)

print(ans)
#
# for k,v in words.items():
#     print(k)
#     print(v)
