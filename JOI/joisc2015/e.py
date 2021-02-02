# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討19分　実装12分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
b = list(map(int,read().split()))

# LIS check
max_num = 0
over_cnt = 0
over_num = -1
for i in b:
    if(i==max_num+1):
        max_num=i
    elif(i==max_num+2):
        over_cnt += 1
        over_num = i
        max_num=i
    elif(i>max_num+2):
        print(0)
        exit(0)

if(over_cnt>1):
    print(0)
    exit(0)
if(over_cnt==1):
    before = 0
    for i,num in enumerate(b,1):
        if(num==over_num-2):
            before = i
            break
    for i,num in enumerate(b,1):
        if(num==over_num):
            print(i-before)
            exit(0)

ans = 1
max_num = 0
for i in b:
    max_num = max(max_num,i)
    ans += max_num
print(ans)

'''
LISとしては、そこまでの最大値+1までの値が並ぶ数列ならなんでもOK。
問題は重複が発生しうること。
そこをうまく管理したい。

BをB1-BiとBi+1-Bn-1に分解。
同じようにB1-BjとBj+1-Bn-1に分解。（i<jとする。）

B1-Bi,x,Bi+1-Bj,Bj+1-Bn-1
B1-Bi,Bi+1-Bj,y,Bj+1-Bn-1
が一致する場合、
Bi+1-Bj-1　==　Bi+2-Bj　なので、
Bi+1～Bjまで同じ値が並ぶ場合は重複する可能性がある。

→→
前のビルと同じ値を突っ込む場合はカウントしなければよい？


それとは別に、LISが作れるかどうかのチェックも必要。

・いままでの最大値+2が1回だけ現れる
　→　ありえるのは1通りのみ
・いままでの最大値+3が現れるorいままでの最大値+2が2回以上現れる
　→　不可



1,2,1,3,1,2,4

4,5,3,6,1,2,7

==========

over_cnt==1の時

1,2,1,1,4
3を突っ込む余地が3か所ある。これだ。

'''
