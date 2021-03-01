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

def input_d(s):
    if '.' in s:
        s1,s2 = s.split('.')
        res = int(s1) * 10000
        res +=  int(s2) *  10 ** (4 - len(s2))
    else:
        res = int(s) * 10000
    return res

x,y,r = map(input_d, input().split())

left = ((-x+r) // 10000 ) * -10000
right = ((x+r) // 10000) * 10000

ans = 0
for i in range(left,right+1,10000):
    d0 = r**2 - (x-i)**2
    d = int(d0**0.5)
    for j in range( max(0,d-3), d+3 ):
        if j**2 > d0:
            d1 = j-1
            break
    up = (y + d1)//10000
    down = (-y + d1)//10000 * -1
    ans += up-down+1
print(ans)





