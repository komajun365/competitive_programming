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

n,a = map(int,input().split())

if n == 1:
    print(1)
    exit()

ans = n
for i in range(1,40):
    l = int(n ** (1/(i+1))) + 2
    while l ** (i+1) >= n:
        l -= 1
    
    for j in range(i+2):
        tmp = (l+1)**j * l**(i+1-j)
        if tmp >= n:
            break
    ans = min(ans, i*a + (l+1)*j + l*(i+1-j))
    # print(i,ans)
print(ans)
    

