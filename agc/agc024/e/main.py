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

n,k,m = map(int,input().split())


'''
dp[i][j] := 数字をi個並べたとき、合計がjとなっているものの数

dp[i][j] = dp[i-1][]


0:1,3,12,60,360
1:0,1,8,58,
2:0,1,8,60,
3:0,1,8,

31:311,312,313,321,331
32:321,322,323,332
33:331,332,333

21:211,212,213,221,231,321
22:221,222,223,232,322
23:231,232,233,323
32:321,322,323,332

11:111,112,113,121,131,211,311
12:121,122,123,132,212,312
13:131,132,133,213,313
21:211,212,213,221,231,321
31:311,312,313,321

dp[i][j] := 合計がiでjが使われている回数
dp[i][j] = sum(dp[i-1])



'''