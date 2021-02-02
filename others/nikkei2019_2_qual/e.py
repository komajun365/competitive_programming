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

n,k = map(int,input().split())

ab = []
for i in range(1,n+1):
    a,b=0,0
    if(n%2==1):
        if(i%2==1):
            a,b = i, n + 1 + (n-i)//2
        else:
            a,b = i, 2*n - (i-2)//2
    elif(n%2==0):
        if(i%2==0):
            a,b = i, n + 1 + (n-i)//2
        else:
            a,b = i, 2*n - i//2
    a += k-1
    b += k-1
    ab.append((a+b,a,b))

ab.sort()

ans = []
for i in range(n):
    c = k+2*n+i
    tot,a,b = ab[i]
    if(tot > c):
        print(-1)
        exit()
    ans.append((a,b,c))

print('\n'.join(map(lambda x: ' '.join(map(str,x)), ans) ))




'''
k - k+3n-1

Ci = k+2n - k+3n-1
としてよさそう。

Cn　から埋めていってよさそう？

1,8
2,10
3,7
4,9
5,6


1,11
2,14
3,10
4,13
5,9
6,12
7,8

なんだこれ・・・

1-8 (11以下)
1,8
2,6
3,7
4,5

1-12( 16以下)
1,12
2,9
3,11
4,8
5,10
6,7


作り方
for i in range(1,k+1):
    if(k%2==1):
        if(i%2==1):
            (i, k + 1 + (k-i)//2)
        else:
            (i, 2k - (i-2)//2)

i + k + 1 + (k-i)//2
(i==k)のとき
2k+1

i +  2k - (i-2)//2
(i==2)のとき
2k+i

for i in range(1,k+1):
    if(k%2==0):
        if(i%2==0):
            (i, n + 1 + (n-i)//2)
        else:
            (i, 2*n - i//2)


i +  n + 1 + (n-i)//2)
(i==n)のとき
2*n+1

i +  2*n - i//2
(i==1)のとき
2*n+1



'''
