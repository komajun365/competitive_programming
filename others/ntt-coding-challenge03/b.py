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

a,b,x,n = map(int,input().split())

def print_yes():
    print('YES')
    exit()

def print_no():
    print('NO')
    exit()

if(n == 0):
    print_yes()

if(a==0):
    print_no()

if(x==1):
    if(a >= n):
        print_yes()
    else:
        print_no()

if(b==0):
    print_no()

if(b==1):
    if(a >= n):
        print_yes()
    else:
        print_no()

x_num = a * b**(x-1)
if(x_num >= n):
    print_yes()
else:
    print_no()
