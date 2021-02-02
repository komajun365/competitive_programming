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

s = input()
base = 'WBWBWWBWBWBW'
base *= 4
ans = {0:'Do',2:'Re',4:'Mi',5:'Fa',7:'So',9:'La',11:'Si' }

for i in range(12):
    if(s == base[i:i+20]):
        print(ans[i])
        exit()