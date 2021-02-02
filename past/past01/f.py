# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

s=input()
words = []
head = -1
for i in range(len(s)):
    if(head==-1):
        head = i
    else:
        if(s[i].isupper()):
            word = s[head:i+1]
            words.append((word.lower() , word))
            head = -1

words.sort()
ans = [i[1] for i in words]
print(''.join(ans))
