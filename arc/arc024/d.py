# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k = map(int,input().split())
s = input()

if(k*2 > n):
    print('NO')
    exit()

def check(p,alp):
    mod = p
    encode = {}
    for i,ch in enumerate(alp,10001):
        encode[ch] = pow(172603,i,mod)

    left = 0
    right = 0
    for i in range(k):
        left += encode[s[i]]
        left %= mod

        right += encode[s[i+k]]
        right %= mod

    words = set()
    for i in range(n):
        # print(i,i+k,i+k*2)
        words.add(left)
        if(right in words):
            # print(p)
            # print(words)
            # print(right)
            return True
        if(i+2*k >= n):
            break
        left += encode[s[i+k]] - encode[s[i]]
        left %= mod
        right += encode[s[i+k*2]] - encode[s[i+k]]
        right %= mod

    return False

ans = True
ps = '9999217 9999221 9999233 9999271 9999277 9999289 9999299 9999317 9999337 9999347 9999397 9999401 9999419 9999433 9999463 9999469 9999481 9999511 9999533 9999593 9999601 9999637 9999653 9999659 9999667 9999677 9999713 9999739 9999749 9999761 9999823 9999863 9999877 9999883 9999889 9999901 9999907 9999929 9999931 9999937 9999943 9999971 9999973'
ps = list(map(int,ps.split(' ')))
ps.append(10**9+7)
ps.append(3040409)
ps.append(10**20+9)
for p in ps:
    for alp in ['qwertyuioplkmnjhbvgfcdxsaz','qazxcsdwertfgvbnmhjyuioklp']:
        ans = (ans& check(p,alp))

if(ans):
    print('YES')
else:
    print('NO')
