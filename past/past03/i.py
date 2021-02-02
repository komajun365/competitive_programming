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

n = int(readline())
q = int(readline())
data = list(map(int,read().split()))

ans = []
t = 0
nums = [list(range(n)),list(range(n))] # i,j

i = 0
max_i = len(data)
while(i < max_i):
    if(data[i]==1):
        a,b = data[i+1:i+3]
        a,b = a-1,b-1
        i += 3
        nums[t][a],nums[t][b] = nums[t][b],nums[t][a]
    elif(data[i]==2):
        a,b = data[i+1:i+3]
        a,b = a-1,b-1
        i += 3
        nums[1-t][a],nums[1-t][b] = nums[1-t][b],nums[1-t][a]
    elif(data[i]==3):
        t = 1-t
        i += 1
    else:
        a,b = data[i+1:i+3]
        a,b = a-1,b-1
        i += 3
        if(t==0):
            ans.append(nums[0][a] * n + nums[1][b])
        else:
            ans.append(nums[0][b] * n + nums[1][a])


print('\n'.join(map(str,ans)))
