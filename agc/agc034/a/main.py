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

n,a,b,c,d = map(int,input().split())
a -= 1
b -= 1
c -= 1
d -= 1
s = input()

if(c > d):
    for i in range(b-1, d):
        tmp = s[i:i+3]
        if(tmp == '...'):
            break
    else:
        print('No')
        exit()


for l,r in zip([a,b],[c,d]):
    for i in range(l,r):
        tmp = s[i:i+2]
        if(tmp == '##'):
            print('No')
            exit()

print('Yes')


