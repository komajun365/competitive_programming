import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k = map(int, input().split())

prob = [1/n] * n

for i in range(n):
    score = i+1
    while(score < k):
        score *= 2
        prob[i] *= 1/2

ans = sum(prob)
print(ans)
