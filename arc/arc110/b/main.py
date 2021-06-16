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
t = input()

if t == '1':
    print(10**10*2)
    exit()

heads = ['1', '11', '']
tails = ['0', '10', '']

for head in heads:
    tmp1 = head + t
    for tail in tails:
        tmp2 = tmp1 + tail
        if len(tmp2) == tmp2.count('110') * 3:
            l = len(tmp2) // 3
            ans = 10**10 - l + 1
            print(ans)
            exit()

print(0)

