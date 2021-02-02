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

n = int(input())
a = list(map(int,input().split()))

def calc(x):
    cumsum = [0] * n
    cumsum[0] = x[0]
    for i in range(n-1):
        cumsum[i+1] = cumsum[i] + x[i+1]
    
    res = [[0,0] for _ in range(n-1)]
    l = 0
    for r in range(1,n-1):
        tot = cumsum[r]
        while(l < r-1):
            if( abs(tot - cumsum[l]*2) > abs(tot - cumsum[l+1]*2) ):
                l += 1
            else:
                break
        
        res[r][0] = cumsum[l]
        res[r][1] = tot - cumsum[l]
    
    return res

ab = calc(a)
cd = calc(a[::-1])

ans = 10**20
for i in range(1,n-2):
    max_n = max(max(ab[i]), max(cd[-i-1]))
    min_n = min(min(ab[i]), min(cd[-i-1]))
    ans = min(ans, max_n-min_n)
print(ans)

# print(ab)
# print(cd)