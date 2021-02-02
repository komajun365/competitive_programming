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
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

n,q = map(int,readline().split())
s = read().split()


encode_abc={'A':0, 'B':1, 'C':2}

def encode(x):
    res = 0
    for i,xi in enumerate(x):
        res += encode_abc[xi] * 3 ** i
    return res

def reverse(x,l):
    y = x % (3**l)
    res = x - y
    for i in range(l-1,-1,-1):
        z = y%3
        res += z*3**i
        y //= 3
    return res
    
rev = [[] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(3**i):
        rev[i].append(reverse(j,i))

dp = [-1] * (3**n)
stack = []
for i in range(n+1):
    for j in range(i,n+1):
        x = 0
        for k in range(i,j):
            x += 3**k
        for k in range(j,n):
            x += 2 * 3**k
        stack.append(x)
        dp[x] = 0

while(stack):
    next = []
    while(stack):
        x = stack.pop()
        for i in range(1,n+1):
            y = x % (3**i)
            # print(i,y)
            cand = x - y + rev[i][y]
            if(dp[cand] != -1):
                continue
            dp[cand] = dp[x] + 1
            next.append(cand)
    stack,next = next,stack

ans = []
for si in s:
    ans.append(dp[ encode(si) ])

print('\n'.join(map(str,ans))) 

# print(rev)
# print(dp)



        


'''
ABCCABCBACBAA





(BCCABCBACB)AAA
ACB(BCCABCB)AAA
BCCABCBBCAAAA
ACCBBCBBCAAAA
(CCBBCBBC)AAAAA
BBCBBCCCAAAAA
CBBCCCBBAAAAA
BBCCCCBBAAAAA
CCCCBBBBAAAAA
AAAAABBBBCCCC

CBBCBBCCAAAAA
BBCCBBCC
CCBBBBCC
BBBBCCCC
CCCCBBBB

'''