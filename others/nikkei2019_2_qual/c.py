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
a = [ [int(s),i]  for i,s in enumerate(input().split())]
b = [ [int(s),i]  for i,s in enumerate(input().split())]
a.sort(reverse=True)
b.sort(reverse=True)

go = [-1] * n

b_ind = 0
ans = 'No'
for a_ind, (j,j_ind) in enumerate(a):
    while(b[b_ind][0] >= j ):
        b_ind += 1

        if(b_ind == n)&(a_ind < n-1):
            print('Yes')
            exit()

        if(b_ind == n):
            break

    if(b_ind == a_ind):
        print('No')
        exit()

    if(b_ind > a_ind+1):
        ans = 'Yes'

    go[j_ind] = b[a_ind][1]


now = 0
cnt = 0
for _ in range(n-1):
    now = go[now]
    cnt += 1
    if(now==0):
        print('Yes')
        exit()

print(ans)


'''
好きな並びにしたいと思ったら？
n-1回あればswapできる
あるいは、二つ以上のループにできるのであれば、
全部移動できる。

Aの中で大きい方から移動先を決めていけばよい？
ループを作れるなら作る？　どうやって？

一つのループでしか動けない場合とは。
大きい方から決めていって、どこかで二つ以上選択肢があればなんとかなる？

1,2,3,4,5
a,b,c,d,e
a,b,d,c,e
2,3,5,4,1

大きい方から決めていく。
最後まで決められない　→　No
最後まで決められる　&　選択肢がずっと一つ　＆　一つのループ　→　No
上以外　→　Yes

'''
