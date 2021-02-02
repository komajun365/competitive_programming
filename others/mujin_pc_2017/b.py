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

n = int(input())
a = [input() for _ in range(n)]

cnt_col = [0]*n
cnt_row = [0]*n

for i in range(n):
    for j in range(n):
        if(a[i][j] == '#'):
            cnt_col[i] += 1
            cnt_row[j] += 1

if(sum(cnt_col)==0):
    print(-1)
    exit()

b_row = cnt_row.count(n)


ans = 2*n
for i in range(n):
    if(cnt_col[i] == n):
        ans = min(ans, n-b_row)
        continue

    if(cnt_row[i] > 0):
        ans = min(ans, n-cnt_col[i] + n-b_row)
    else:
        ans = min(ans, n-cnt_col[i] + n-b_row + 1)

print(ans)




'''

行をコピーして転置して貼り付け

1行まるまる黒にするのが必須
それができれば全部黒にはできる

最小かどうかはわからない・・・

一個でも黒があれば、２N-1回で全部黒にできる


・1行全部黒の行がある
→　黒じゃない列を全部塗って終わり

・1行全部黒の行がない
→　1行全部黒にするまでに、どこかの列を全部黒にできる？
　→　できない。

というわけで、「1行全部黒の行」を作るまでに何回必要か、が重要。

i行目を黒にするのに、何回必要？がわかればよい？
・i列目が黒の行がある？
　→　そこをうまく使えばOK
。i列目が黒の行がない
　→　どこでもいいから黒を持ってきてi列目に貼る
　　（i,i）が黒で白に戻ることある？
　　→　（i,i）が黒なら「i列目が黒の行がない」に矛盾してるから考えなくてよい。


'''
