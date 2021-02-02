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

def z_algorithm(s):
    n = len(s)
    if(n == 0):
        return []
    if(type(s) is str):
        s2 = [0] * n
        for i, si in enumerate(s):
            s2[i] = ord(si)
        s = s2
    z = [0] * n
    j = 0
    for i in range(1, n):
        z[i] = 0 if (j + z[j] <= i) else min(j + z[j] - i, z[i - j])
        while(i + z[i] < n):
            if(s[z[i]] != s[i + z[i]]):
                break
            z[i] += 1
        if(j + z[j] < i + z[i]):
            j = i
    z[0] = n
    return z

s = input()
z = z_algorithm(s)
print(*z)
