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

fac = [1] * 10
for i in range(1,10):
    fac[i] = fac[i-1] * i

print(fac)

def solve(fac):
    ans = []
    for i in range(10,fac[9]*7+10):
        tmp = 0
        x = i
        while(x>0):
            tmp += fac[x%10]
            x //= 10
        if(i==tmp):
            ans.append(tmp)
    print(ans)
    print(sum(ans))

solve(fac)

fac[0] = 0
solve(fac)

'''
みんな大好き全探索
9! * 7まで探索する。


'''
