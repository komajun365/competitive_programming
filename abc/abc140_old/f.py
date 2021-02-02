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

n = int(input())
s = list(map(int,input().split()))
s.sort(reverse=True)
nums = [0] * 2**n

def next_combination(sub):
    x = sub & -sub
    y = sub + x
    return (((sub & ~y) // x) >> 1) | y

ind = 0
for i in range(n,0,-1):
    j = (1<<i) -1
    while(j < 2**n):
        print(j)
        nums[j] = s[ind]
        ind += 1
        j = next_combination(j)

nums[0] = s[ind]

while(len(nums) > 1):
    new = []
    it = iter(nums)
    for l,r in zip(it,it):
        if(l>=r):
            print('No')
            exit()
        new.append(r)

    nums = new

print('Yes')



# for i in range(n):
#     j = (1<<i)-1
