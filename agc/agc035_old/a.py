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

n = int(input())
a = list(map(int,input().split()))

def print_end(x):
    pr = ['No','Yes']
    print(pr[x])
    exit()

if(sum(a)==0):
    print_end(1)

if(n%3!=0):
    print_end(0)

set_a = set(a)
if(len(set_a)==1)|(len(set_a)>3):
    print_end(0)

if(len(set_a)==2):
    a0,a1 = sorted(list(set_a))
    if(a0!=0):
        print_end(0)
    if(a.count(a0) * 2 == a.count(a1)):
        print_end(1)
    print_end(0)
else:
    a0,a1,a2 = sorted(list(set_a))
    if(a.count(a0) == a.count(a1) == a.count(a2))&((a0^a1)==a2):
        print_end(1)
    print_end(0)
