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
# f = open('../../input.txt', 'r')
# sys.stdin = f

# https://github.com/E869120/kyopro_educational_90/blob/main/sample/006.txt

from collections import deque

def solve(s,k):
    n = len(s)
    w = n-k
    ans = []
    dq = deque()

    def add(si,idx):
        while dq:
            if dq[-1][0] > si:
                dq.pop()
            else:
                break
        dq.append([si,idx])
        # print(dq)

    for i in range(w):
        si = s[i]
        add(si,i)
        
    for i in range(w,n):
        si = s[i]
        add(si,i)
        x,_ = dq.popleft()
        ans.append(x)

    print(''.join(ans))

solve('atcoder',3)
solve('competitiveprogramming',5)
solve('competitiveprogramming',10)
solve('competitiveprogramming',22)

