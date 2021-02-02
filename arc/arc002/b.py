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

from datetime import datetime, date, timedelta
s = input()

today = datetime.strptime(s, '%Y/%m/%d')
while(True):
    today_s = datetime.strftime(today, '%Y/%m/%d')
    y,m,d = map(int,today_s.split('/'))
    if(y%(m*d)==0):
        print(today_s)
        exit()
    today = today + timedelta(days=1)
