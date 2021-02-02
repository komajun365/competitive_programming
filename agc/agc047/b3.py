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
data = read().split()
data.sort(key= lambda x: len(x))

base = ord('a')
s = [[] for _ in range(n)]
for i,si in enumerate(data):
    num = 0
    for ch in si:
        s[i].append(ord(ch)-base+1)

s_tails = [[] for _ in range(n)]
for i,si in enumerate(s):
    s_tails[i].append(0)
    now = 0
    for j,si_j in enumerate(si[1:][::-1]):
        now += si_j * pow(27,j)
        s_tails[i].append(now)

words = dict()

ans = 0
for si,s_tail in zip(s,s_tails):
    head = si[0]

    heads = set()
    heads.add(head)

    for i,num in enumerate(s_tail[::-1],1):
        if( num in words):
            word = words[num]
            for j in heads:
                if(j in word):
                    ans += word[j]
        if(i==len(si)):
            break
        heads.add(si[i])

    if(not s_tail[-1] in words):
        words[s_tail[-1]] = dict()

    if(not head in words[s_tail[-1]]):
        words[s_tail[-1]][head] = 1
    else:
        words[s_tail[-1]][head] += 1

    # print(si,ans)

print(ans)

# for k,v in words.items():
#     print(k)
#     print(v)
#
# print(s)
#
# print(s_tails)
