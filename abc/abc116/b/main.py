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

s = int(input())
done = [0] * (10**6+1)
done[s] = 1
for i in range(2,10**6+2):
    if(s%2==0):
        s = s//2
    else:
        s = 3*s+1
    if(done[s]==1):
        print(i)
        exit()
    done[s] = 1
    # print(s)

