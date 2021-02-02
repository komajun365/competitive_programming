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

import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

t = int(readline())

def get_base(x,basis):
    for b in basis:
        x = min(x,x^b)
    return x

for _ in range(t):
    n = int(readline())
    a = list(map(int,readline().split()))
    s = readline().strip()

    basis = []
    for si,ai in zip(s[::-1], a[::-1]):
        x = get_base(ai,basis)
        if(si=='0')&(x>0):
            basis.append(x)
        elif(si=='1')&(x>0):
            print(1)
            break
    else:
        print(0)



'''
xor の掃き出しすごい簡単に出来るんですね

vector<int> basis;
for(int e : a){
  for(int b : basis)
    chmin(e, e ^ b);
  if(e)
    basis.push_back(e);
}

これで数列 a の基底が basis に入る

6:05pm · 30 Nov 2019 · Twitter for iPhone


for e in a:
    for b in basis:
        e = min(e,e^b)
    if(e):
        basis.append(e)

'''
