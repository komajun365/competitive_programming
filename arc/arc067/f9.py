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

def main():
    from sys import stdin
    read = stdin.buffer.read
    readline = stdin.buffer.readline
    from collections import defaultdict
    from itertools import accumulate

    n,m = map(int,readline().split())
    a = tuple(map(int,readline().split()))
    b = tuple(map(int,read().split()))

    query = [defaultdict(int) for _ in range(n+2)]

    for i in range(m):
        left = list(range(-1,n+1))
        right = list(range(1,n+3))

        bi = [(val,j) for j,val in enumerate(b[i::m], 1)]
        bi.sort()
        for val,j in bi:
            l = left[j]
            r = right[j]
            query[l+1][j] += val
            query[l+1][r] -= val
            query[j+1][j] -= val
            query[j+1][r] += val
            right[l] = r
            left[r] = l

    imos = [0] * (n+2)
    for i,ai in enumerate(a,2):
        imos[i] = imos[i-1] - ai
        query[i][i] += ai

    ans = 0
    for i in range(1,n+1):
        next = [0] * (n+3-i)
        for j,val in query[i].items():
            next[j+1-i] += val

        for j,val in enumerate(accumulate(next),i-1):
            imos[j] += val
        ans = max(ans, max(imos[i:n+1]))

    print(ans)

if __name__ == '__main__':
    main()
