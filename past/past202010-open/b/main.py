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

x,y = map(int,input().split())
if(y==0):
    print('ERROR')
    exit()

ans = x*100//y
ans0 = ans//100
ans1 = ans%100
ans0 = str(ans0)
if(ans1 < 10):
    ans1 = '0' + str(ans1)
else:
    ans1 = str(ans1)
print(ans0 + '.' + ans1) 