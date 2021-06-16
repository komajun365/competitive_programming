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
a = list(map(int,input().split()))

cnt = [0] * n
for ai in a:
    cnt[ai] += 1

for i in range(n):
    if cnt[i] > 0:
        min_num = i
        break

if cnt[min_num] == 1:
    if min_num * 2 + 1 > n:
        print('Impossible')
        exit()
    for i in range(min_num+1, min_num*2+1):
        if cnt[i] < 2:
            print('Impossible')
            exit()
    
    for i in range(min_num*2+1, n):
        if cnt[i] > 0:
            print('Impossible')
            exit()
elif cnt[min_num] == 2:
    if min_num * 2 > n:
        print('Impossible')
        exit()
    for i in range(min_num+1, min_num*2):
        if cnt[i] < 2:
            print('Impossible')
            exit()
    
    for i in range(min_num*2, n):
        if cnt[i] > 0:
            print('Impossible')
            exit()

else:
    print('Impossible')
    exit()

print('Possible')
    
