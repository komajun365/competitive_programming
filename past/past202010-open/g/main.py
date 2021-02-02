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

n,m = map(int,input().split())
s = []
for _ in range(n):
    s.append(input())

num = 0
for si in s:
    num += si.count('.')

def calc(x,y):
    stack = [x*m+y]
    res = 0
    done = [[0] * m for _ in range(n)]
    done[x][y] = 1
    while(stack):
        i,j = divmod(stack.pop(),m)
        for i2,j2 in zip([0,0,-1,1],[-1,1,0,0]):
            i2 += i
            j2 += j
            if(i2<0) or (i2>=n) or (j2 < 0) or (j2 >= m):
                continue
            if(done[i2][j2] != 0) or s[i2][j2] == '#':
                continue
            done[i2][j2] = 1
            stack.append(i2*m+j2)
            res +=1
    return res

ans = 0
for i in range(n):
    for j in range(m):
        if(s[i][j] == '#'):
            if(num == calc(i,j)):
                ans += 1
print(ans)


