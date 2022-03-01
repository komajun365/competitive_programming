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
b = list(map(int,input().split()))

def check(x):
    db = dict()
    for bi in b:
        db[bi] = db.get(bi, 0) + 1
    for ai in a:
        if db.get(x ^ ai, 0) == 0:
            return 0
        db[x ^ ai] -= 1
    return 1

tot = 0
for ai in a:
    tot ^= ai
for bi in b:
    tot ^= bi

if n % 2 == 1:
    ans = check(tot)
    print(ans)
    if ans == 1:
        print(tot)
    exit()

if tot != 0:
    print(0)
    exit()

nums = set()
for i in range(n):
    cand = tot ^ a[0] ^ b[i]
    if check(cand) == 1:
        nums.add(cand)

nums = list(nums)
nums.sort()
print(len(nums))
for ni in nums:
    print(ni)
    
