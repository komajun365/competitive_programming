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

n=int(input())
import sys
b=list(map(int,sys.stdin.read().split()))
x=1
m=0
p=0
q=0
o=[n]*(n+1)
o[0]=-1
for i,j in enumerate(b):
    o[j]=min(o[j],i)
    if(j>m+1):p,q=p+j-m-1,j
    m=max(m,j)
    x+=m
if(p>1):x=0
if(p==1):x=o[q]-o[q-2]
print(x)



# import sys;n,*b=list(map(int,sys.stdin.read().split()));x=1;m=p=q=0;o=[n]*(n+1);o[0]=-1
# for i,j in enumerate(b):
#  if(j>m+1):p,q=p+j-m-1,j
#  m=max(m,j);
#  x+=m;o[j]=min(o[j],i)
# if(p):x=o[q]-o[q-2]*(p==1)
# print(x)
#
# print(o)

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
