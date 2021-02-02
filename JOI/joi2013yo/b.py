# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

m,n = map(int, input().split())
s = input()
t = input()
s += '?'
t += '?'

dp_i = [[0] * (n+2) for _ in range(m+2)]
dp_o = [[0] * (n+2) for _ in range(m+2)]

for i in range(m,-1,-1):
    for j in range(n,-1,-1):
        dp_i[i][j] = max( dp_o[i+1][j]+1 if s[i]=='I' else 0 ,
                          dp_o[i][j+1]+1 if t[j]=='I' else 0)
        dp_o[i][j] = max( dp_i[i+1][j]+1 if s[i]=='O' else 0 ,
                          dp_i[i][j+1]+1 if t[j]=='O' else 0)

ans = max( map(max, dp_i))
# ans = 0 if ans==0 else ans - (ans%2==0)
print(ans)

'''
方針
dp。
車庫Sからi台を待機に回し、
車庫Tからj台を待機に回した状態を考える。
dp_i[i][j] ： 上記の状態で'I'から始めたときにつなげる最大の車両数
dp_o[i][j] ： 上記の状態で'O'から始めたときにつなげる最大の車両数
とすると

dp_i[i][j] = max( dp_o[i+1][j]+1 if s[i]=='I' else 0 ,
                  dp_o[i][j+1]+1 if t[j]=='I' else 0)
で更新できる。

車庫S,車庫Tともに、最後尾にIでもOでもないダミー車両を追加しておくと、
dpの更新における場合分けが少なく済む。

dp_iの中の最大値を超えない奇数が答え。
(車両Iが一つもないときだけコーナーケースになるので気を付ける。)
'''
