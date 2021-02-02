import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

def calc_(x,n):
    ans = 0
    for i in range(n-1):
        ans += x[i] - 1
        ans *= (n-1-i)
        for j in range(i+1 , n):
            if(x[j] > x[i]):
                x[j] -= 1
    return ans

print( abs(calc_(p,n) - calc_(q,n)))
