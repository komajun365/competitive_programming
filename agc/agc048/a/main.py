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

t = int(input())
atc = 'atcoder'
for _ in range(t):
    s = input()
    n = len(s)

    i = 0
    ans = 10000
    for cnt in range(min(n,7)):
        if(atc[i] == s[i]):
            i += 1
            continue
        elif(atc[i] < s[i]):
            ans = 0
            i = 0
            break
        else:
            i += 1
            break
    else:
        if(n > 7):
            ans = 0
            i = 0
    for j in range(i):
        for k in range(j+1, n):
            if(atc[j] < s[k]):
                ans = min(ans, k-j)
                break
    if ans == 10000:
        print(-1)
    else:
        print(ans)

    


