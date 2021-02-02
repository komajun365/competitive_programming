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
f = open('p018_triangle.txt', 'r')
sys.stdin = f

import itertools
ans = set()
for p in itertools.permutations(range(1,10)):
    for a,b,c in [[1,4,4],[2,3,4]]:
        num_a = 0
        num_b = 0
        num_c = 0
        for i in range(0,a):
            num_a = num_a*10 + p[i]
        for i in range(a,a+b):
            num_b = num_b*10 + p[i]
        for i in range(a+b,a+b+c):
            num_c = num_c*10 + p[i]

        if(num_a*num_b==num_c):
            ans.add(num_c)

print(ans)
print(sum(ans))


'''
数字9個の順列＝3.6*10**5
[1,4,4]
[2,3,4]
この分け方で調べてみましょう。

'''
