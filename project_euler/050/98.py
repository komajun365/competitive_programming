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
f = open('words.txt', 'r')
sys.stdin = f

from collections import defaultdict
d = defaultdict(lambda : [])

s = input().split(',')
s = list(map(lambda x: x.strip('\"'), s))

print(s[:10])
print(len(s))

longest = ''
for si in s:
    if(len(longest) < len(si)):
        longest = si
print(longest)

for si in s:
    d[''.join(sorted(si))].append(si)

cand = []
for key,val in d.items():
    if(len(val) == 2):
        cand.append(val)
    elif(len(val) == 3):
        cand.append(val[0:2])
        cand.append(val[1:3])
        cand.append(val[::2])


print(cand)
print(len(cand))
print( max(map(lambda x: len(x[0]),cand)))

squares = [set() for _ in range(11)]
for i in range(10**5):
    i2 = i**2
    squares[(len(str(i2)))].add(i2)

print(squares[:2])
for i in range(11):
    print(i,len(squares[i]))

ans = 0
for xy in cand:
    # print(xy)
    x,y = xy
    len_n = len(x)
    for num in squares[len_n]:
        dic = [''] * 10
        s_num = str(num)
        for i in range(len_n):
            if( dic[int(s_num[i])] == '' ):
                dic[int(s_num[i])] = x[i]
            else:
                if(x[i] != dic[int(s_num[i])]):
                    break
        else:
            dic2 = {}
            for ind,j in enumerate(dic):
                if(j != ''):
                    dic2[j] = ind
            change = 0
            for i in range(len_n):
                change *= 10
                change += dic2[y[i]]
            if(change in squares[len_n]):
                ans = max(ans, num, change)
                print(x,y,num,change)

print(ans)

for num in squares[5]:
    s_num = str(num)
    check = 1
    for i in [1,7,6,8,9]:
        check *= s_num.count(str(i))
    if(check):
        print(num)

print('================')

for xy in [['BOARD', 'BROAD']]:
    # print(xy)
    x,y = xy
    len_n = len(x)
    for num in [18769]:
        dic = [''] * 10
        s_num = str(num)
        for i in range(len_n):
            if( dic[int(s_num[i])] == '' ):
                dic[int(s_num[i])] = x[i]
            else:
                if(x[i] != dic[int(s_num[i])]):
                    break
        else:
            print('================')
            dic2 = {}
            for ind,j in enumerate(dic):
                if(j != ''):
                    dic2[j] = ind
            change = 0
            for i in range(len_n):
                change *= 10
                change += dic2[y[i]]
            print(change)
            if(change in squares[len_n]):
                ans = max(ans, num, change)
                print(x,y,num,change)




'''
アナグラムグループを作る。




'''
