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

c = input()

if(c=='a')|(c=='z'*20):
    print('NO')
    exit()

if(len(set(c)) != 1):
    c2 = []
    for ci in c:
        c2.append(ci)
    c2.sort()
    ans = ''.join(c2)

    if(c==ans):
        ans = ans[::-1]

elif(len(c)==1):
    ans = 'a' + chr(ord(c[0]) - 1)

else:
    c_num = 0
    for ci in c:
        c_num += ord(ci) - ord('a') + 1

    ans = ''
    while(c_num > 26):
        ans += 'z'
        c_num -= 26
    ans += chr( ord('a') + c_num - 1 )

print(ans)
