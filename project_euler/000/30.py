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
f = open('p018_triangle.txt', 'r')
sys.stdin = f

print(9**5)
ex5 = [i**5 for i in range(10)]

ans = []
for i in range(10,6 * 9**5 + 1):
    x = i
    y = 0
    while(x>0):
        y += ex5[x%10]
        x //= 10
    if(i==y):
        ans.append(i)

print(ans)
print(sum(ans))


'''
全探索じゃ
9**5が59049なので、
9**5*6まで探索するよ
'''
