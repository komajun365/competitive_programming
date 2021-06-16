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
import glob

solve = 'A'

def sol(i):
    f_in = open(i,'r')
    sys.stdin = f_in

    a = int(input())
    b = 180 - (180-a)//2

    print(b)


in_dir = './{}/input/*'.format(solve)
in_list = glob.glob(in_dir)

for i in in_list:
    print(i)
    j = i.replace('in','out')

    sol(i)
    f_out = open(j,'r')
    print(f_out.read())




# f = open('../../input.txt', 'r')
# sys.stdin = f
