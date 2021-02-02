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

v,t,p = map(int,input().split())
ans = v*(p+1)
ans += 1 + ans//(t-1) - (ans%(t-1)==0)
print(ans)

'''
鼻水をすすらないとき
V*(P+1)秒耐えられる。
0秒、(t-1)秒、2(t-1)秒,...のタイミングで1秒待ったをかけられる。
ただし、V*(P+1)秒目は耐えられない。

OK？


'''
