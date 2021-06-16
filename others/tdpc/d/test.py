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

import sys
sys.setrecursionlimit(10**9)
from functools import lru_cache
import random

def solve1(n,d):
    x = d
    cnt = dict()
    for i in [2,3,5]:
        cnt[i] = 0
        while x%i == 0:
            x //= i
            cnt[i] += 1

    if x != 1:
        return 0
        # print(0)

    @lru_cache(maxsize=10**9)
    def solve(x,a,b,c):
        a = max(a,0)
        b = max(b,0)
        c = max(c,0)
        if a == b == c == 0:
            return 1
        if x == 0:
            return 0
        res = 0
        res += solve(x-1,a,b,c)
        res += solve(x-1,a-1,b,c)
        res += solve(x-1,a,b-1,c)
        res += solve(x-1,a-2,b,c)
        res += solve(x-1,a,b,c-1)
        res += solve(x-1,a-1,b-1,c)
        return res/6

    ans = solve(n,cnt[2],cnt[3],cnt[5])
    # print(ans)
    return ans

def solve_simple(n,d):
    nums = [1]
    for i in range(n):
        nums2 = []
        for x in nums:
            for y in range(1,7):
                nums2.append(x*y)
        nums,nums2 = nums2,nums
    
    ans = 0
    for x in nums:
        if x % d == 0:
            ans += 1
    
    return ans / len(nums)

eps = 0.000001
for _ in range(1000):
    n = random.randint(1,6)
    # d = random.randint(1,100)
    d2 = random.randint(1,10)
    d3 = random.randint(1,5)
    d5 = random.randint(1,5)
    d = d2*d3*d5
    ans1 = solve1(n,d)
    ans2 = solve_simple(n,d)
    if abs(ans1 - ans2) > eps:
        print(n,d)
        print(ans1)
        print(ans2)
        exit()
