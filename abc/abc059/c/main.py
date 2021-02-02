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

ans = 10**20
for x in [0,1]:
    now = 0
    tmp = 0
    for i,ai in enumerate(a):
        now += ai
        if((x+i)%2):
            # +
            if(now <= 0):
                tmp += 1-now
                now = 1
        else:
            # -
            if(now >= 0):
                tmp += now+1
                now = -1
        # print(i,ai,now,tmp)
    ans = min(ans,tmp)
print(ans)
        


