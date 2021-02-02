# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(max(sum(a),sum(b)))
