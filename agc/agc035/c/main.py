# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

n = int(input())
bsf = 0

for i in range(20):
    if(n == 2**i):
        print('No')
        exit()
    if(n >= 2**i):
        bsf = 2**i

print('Yes')
if( n == bsf*2-1):
    for i in range(1,2*n):
        print('{} {}'.format(i,i+1))
    exit()

tot = 0
if(n%2==0):
    m = n-1
else:
    m = n
for i in range(bsf,m+1):
    tot ^= i

if(tot == 0):
    if(n%2==0):
        head = bsf
        neigh = n ^ bsf
        tmp = [head, neigh]
        for i in range(1,m+1):
            if i != head and i != neigh:
                tmp.append(i)
        tmp.append(head+n)
        tmp.append(neigh+n)
        for i in range(1,m+1):
            if i != head and i != neigh:
                tmp.append(i+n)
        for i in range(len(tmp)-1):
            print('{} {}'.format(tmp[i],tmp[i+1]))
        print('{} {}'.format(head,n))
        print('{} {}'.format(neigh,n*2))

    else:
        for i in range(1,2*n):
            print('{} {}'.format(i,i+1))
    exit()

neigh = 1 if tot != 1 else 2
if(n%2==0):
    neigh = n ^ bsf ^ tot

ans = []
tmp = []
for base in [0,n]:
    tmp.append(tot+base)
    tmp.append(neigh+base)
    for i in range(1,bsf):
        if i != tot and i != neigh:
            tmp.append(i+base)
for i in range(len(tmp)-1):
    ans.append([tmp[i],tmp[i+1]])

tmp = [tot]
for i in range(bsf,m+1):
    tmp.append(i)
for i in range(len(tmp)-1):
    ans.append([tmp[i],tmp[i+1]])

tmp = [tot]
for i in range(bsf,m+1)[::-1]:
    tmp.append(i+n)
for i in range(len(tmp)-1):
    ans.append([tmp[i],tmp[i+1]])


if(n%2==0):
    ans.append([bsf,n])
    ans.append([neigh,n*2])

for ai in ans:
    print(*ai , sep=' ')