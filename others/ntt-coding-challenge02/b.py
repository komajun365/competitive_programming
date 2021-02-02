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

# 再帰関数の上限解除
import sys
sys.setrecursionlimit(10**9)

n = int(input())
p = input()
lim = 10**6

xy = [0,0]
dir = 'U'
dir_dic = {'U':[0,1],'D':[0,-1],'L':[-1,0],'R':[1,0]}
URDL = {'U':0,'R':1,'D':2,'L':3}

def done(ch,xy,dir):
    if(ch=='F'):
        xy[0] += dir_dic[dir][0]
        xy[1] += dir_dic[dir][1]
    elif(ch=='B'):
        xy[0] -= dir_dic[dir][0]
        xy[1] -= dir_dic[dir][1]
    elif(ch=='R'):
        dir = 'URDL'[(URDL[dir] + 1)%4]
    elif(ch=='L'):
        dir = 'URDL'[(URDL[dir] - 1)%4]

    # print(ch,xy,dir)
    return xy,dir

def calc(s,xy,dir,cnt):
    point = 0
    while(point < len(s)):
        # print(point)
        # print(xy,dir,cnt)
        now = s[point]
        cyc = 1
        if (now in '23456789'):
            cyc = int(now)
            point += 1
            now = s[point]

        if(now in 'FBRL'):
            for i in range(cyc):
                xy,dir = done(now,xy,dir)
                cnt += 1
                if(cnt >= lim):
                    print(' '.join(map(str,xy)))
                    exit()
            point += 1

        if(now == '['):
            lk = 1
            rk = 0
            point_r = point+1
            while(lk>rk):
                if(s[point_r] == '['):
                    lk += 1
                elif(s[point_r] == ']'):
                    rk += 1
                point_r += 1
            s2 = s[point+1:point_r-1]
            for i in range(cyc):
                xy,dir,cnt = calc(s2,xy,dir,cnt)
                if(cnt >= lim):
                    print(' '.join(map(str,xy)))
                    exit()
            point = point_r

    return xy,dir,cnt


cnt = 0
pointer = 0
xy,dir,cnt = calc(p,xy,dir,cnt)

print(' '.join(map(str,xy)))

#
# while(point < len(s)):
#     now = s[point]
#
#
#
# def calc(s,x,y,dir):
#     point = 0
#     while(point < len(s)):
#         now = s[point]
