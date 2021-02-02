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
p = 89
mod = 1_000_000_009 * 1_000_000_007

s.sort(key= lambda x: len(x))

s_list = []
s_hash_list = []
for si in s:
    s_list.append([])
    s_hash_list.append([0])
    for j in si[::-1]:
        num = ord(j)-ord('a')
        s_list[-1].append(num)
        s_hash_list[-1].append((s_hash_list[-1][-1] * p + num +1) % mod)
    s_hash_list[-1].pop()

words = [dict() for _ in range(26)]
ans = 0
for si,shi in zip(s_list,s_hash_list):
    head = si.pop()
    hash = shi.pop()
    if(hash in words[head]):
        words[head][hash] += 1
    else:
        words[head][hash] = 1

    heads = set()
    heads.add(head)
    while(si):
        heads.add(si.pop())
        hash = shi.pop()
        for hi in heads:
            if(hash in words[hi]):
                ans += words[hi][hash]

print(ans)
