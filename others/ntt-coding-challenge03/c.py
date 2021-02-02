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

n,a,b,c = map(int,input().split())

def print_yes():
    print('YES')
    exit()

def print_no():
    print('NO')
    exit()

n3,n2 = n,n

#3
if(n3 < a):
    print_no()
n3 -= a

if(n2 < b):
    n3 -= (b-n2)
    n2 = 0
else:
    n2 -= b

if(n3*2 + n2 < c):
    print_no()
else:
    print_yes()






'''
3人組は確定
2人組も2席から使う貪欲でOK

'''
