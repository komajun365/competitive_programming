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
p = list(map(int,input().split()))

ind = [0] * (n+1)
for i,pi in enumerate(p):
    ind[pi] = i

inf = 10**9
tn = 2 ** ((n-1).bit_length())
tree = [[inf,inf,0] for _ in range(tn)]
for i in range(n):
    tree[(tn+i)//2][i%2] = p[i]

if(n%2==1):
    tree[(tn+n-1)//2][2] = 1

def update(i):
    l = tree[i*2]
    r = tree[i*2+1]
    if(l[2]==0):
        tree[i][0] = min(l[0],r[0])
        tree[i][1] = min(l[1],r[1])
        tree[i][2] = r[2]
    else:
        tree[i][0] = min(l[0],r[1])
        tree[i][1] = r[0]
        tree[i][2] = (1 + r[2])%2

for i in range(tn//2 -1, 0, -1):
    update(i)

print(tree)

ans = []
for _ in range(n//2):
    num1,num2 = tree[1][:2]
    ans += [num1,num2]

    for i in [num1,num2]:
        i = ind[i]
        if(i%2==0):
            tree[(tn+i)//2][0] = tree[(tn+i)//2][1]
            tree[(tn+i)//2][1] = inf
            if( tree[(tn+i)//2][0] != inf):
                ind[tree[(tn+i)//2][0]] -= 1
        else:
            tree[(tn+i)//2][1] = inf
        tree[(tn+i)//2][2] += 1
        tree[(tn+i)//2][2] %= 2
        i = (tn+i)//4
        while(i>0):
            update(i)
            i //= 2

    print(tree)

print(ans)








'''
4,3,8,7
6,2,5,1



よくわからん二部木を作っていきます。。。

(i,j,k) := iが奇数番目で一番小さい数字、jが偶数番目で一番小さい数字。
　　　　　　kが0のときは全体で偶数個あり、1の時は奇数個ある。
　　　　　　k=1のときは、結合時に斑点が必要になる。

'''
