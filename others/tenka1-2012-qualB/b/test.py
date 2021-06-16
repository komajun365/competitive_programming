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

# s = input()
def solve(s):
    s0 = s[::]

    if s.count('__') > 0:
        return s
        print(s)
        exit()
    if len(s) == 1:
        return s
        print(s)
        exit()

    head = ''
    tail = ''
    if s[0] == '_':
        head = '_'
        s = s[1:]
    if s[-1] == '_':
        tail = '_'
        s = s[:-1]

    if s.count('_') > 0:
        cs = s.split('_')
        ans = ''
        for i in cs:
            l = len(i)
            if not i[0].islower():
                return s0
                print(s0)
                exit()
            tmp = i[0].upper()
            for j in range(1,l):
                if i[j].isupper():
                    return s0
                    print(s0)
                    exit()
                tmp += i[j]
            ans += tmp
        ans = head + ans[0].lower() + ans[1:] + tail
    else:
        if not s[0].islower():
            return s0
            print(s0)
            exit()
        snakes = []
        l = len(s)
        tmp = ''
        for i in range(l):
            if s[i].isupper():
                snakes.append(tmp)
                tmp = s[i].lower()
            else:
                tmp += s[i]
        else:
            snakes.append(tmp)
        ans = head + '_'.join(snakes) + tail

    return ans
    print(ans)

# print('0'.islower())
# print('A'.islower())
# print('a'.islower())
# print('_'.islower())
# print('0'.isupper())
# print('A'.isupper())
# print('a'.isupper())
# print('_'.isupper())

import random
base = 'abcdefghijkLM0_'

for _ in range(100):
    n = random.randint(1,20)
    s = ''
    for _ in range(n):
        s += base[random.randint(0,14)]
    s1 = solve(s)
    s2 = solve(s1)
    if s != s2:
        print(s,s1,s2)
        exit()
    if s != s1:
        print(s,s1)