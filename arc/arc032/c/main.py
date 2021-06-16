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

import sys
read = sys.stdin.buffer.read

n,*data = map(int,read().split())

ab = []
for i in range(1,n+1):
    a,b = data[i*2-2:i*2]
    ab.append([a,b,i])
ab.sort(key = lambda x : x[0])

m = 10**6 + 2
done = [0] * m
last = [[-1,-1] for _ in range(m)]

idx = n-1
for i in range(m-2,-1,-1):
    done[i] = done[i+1]
    last[i] = last[i+1][::]
    while idx >= 0:
        if ab[idx][0] < i:
            break
        a,b,num = ab[idx]
        idx -= 1

        if done[a] < done[b] + 1:
            done[a] = done[b] + 1
            last[a] = [b,num]
        elif done[a] == done[b] + 1:
            if num < last[i][1]:
                last[a] = [b,num]

ans = []
i = 0
while last[i][0] != -1:
    i,task = last[i]
    ans.append(task)
print(len(ans))
print(' '.join(map(str,ans)))


# print(last[:10])
# print(done[:10])

# print(ab)
