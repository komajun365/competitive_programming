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

s = input()
x = int(input()) - 1
n = len(s)

done = [-1]
for i in range(n):
    if s[i] in '123456789':
        done.append((done[-1]+1) * (int(s[i])+1) -1)
    else:
        done.append(done[-1] + 1)
    
    if done[-1] >= x:
        break

while i >= 0:
    # print(x,done)
    if s[i] in '123456789':
        done.pop()
        x %= done[-1]+1
    else:
        if done[-1] == x:
            print(s[i])
            exit()
        done.pop()
    i -= 1

# print(done)
    
        
