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
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def main():

    n,m = map(int,readline().split())
    a = list(map(int,readline().split()))
    a += [0,0,0]
    b = [list(map(int,i.split())) for i in  readlines()]

    imos = [[0] * (n+2) for _ in range(n+2)]
    left = [0] * (n+2)
    right = [0] * (n+2)
    bi = [[0,0] for _ in range(n)]

    for i in range(m):
        for j in range(n+2):
            left[j] = j-1
            right[j] = j+1

        for j in range(n):
            bi[j][0] = b[j][i]
            bi[j][1] = j+1
        bi.sort()
        for val,j in bi:
            l = left[j]
            r = right[j]
            imos[l+1][j] += val
            imos[l+1][r] -= val
            imos[j+1][j] -= val
            imos[j+1][r] += val
            right[l] = r
            left[r] = l

    for i in range(n+1):
        for j in range(1,n+1):
            imos[i][j] += imos[i][j-1]

    for i in range(1,n+1):
        for j in range(n+1):
            imos[i][j] += imos[i-1][j]

    ans = 0
    for i in range(1,n+1):
        dif = 0
        for j in range(i,n+1):
            ans = max(ans,imos[i][j] - dif)
            dif += a[j-1]

    print(ans)


if __name__ == '__main__':
    main()

# for i in imos:
#     print(i)




'''
i~jの焼き肉店に行くときのおいしさの最大値が知りたい




'''
