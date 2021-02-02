import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
b = [int(input()) for _ in range(n)]

check = [[0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],
        [2,5,8],
        [0,4,8],[2,4,6]]

for tmp in check:
    count = 0
    for num in tmp:
        i = num//3
        j = num%3
        if(a[i][j] in b) == False:
            break
        count+=1
        if(count == 3):
            print('Yes')
            exit()

print('No')
