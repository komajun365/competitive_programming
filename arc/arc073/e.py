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

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
xy = list(map(int,read().split()))

if(n==1):
    print(0)
    exit()

max_num = max(xy)
min_num = min(xy)

max_ind = -1
min_ind = -1
same = False
big = []
small = []
for i in range(n):
    x,y = xy[i*2:i*2+2]
    if(x>y):
        x,y = y,x

    if(x==min_num)&(y==max_num):
        same = True

    if(x==min_num):
        min_ind = i
    if(y==max_num):
        max_ind = i

    big.append(y)
    small.append(x)

#最大と最小を違う色に塗る
ans = (max(big)-min(big)) * (max(small) - min(small))
if(same):
    print(ans)
    exit()

#同じ色に塗る
r = max_num - min_num
if(xy[min_ind*2]==min_num):
    min_pair = xy[min_ind*2+1]
else:
    min_pair = xy[min_ind*2]

if(xy[max_ind*2]==max_num):
    max_pair = xy[max_ind*2+1]
else:
    max_pair = xy[max_ind*2]

nums = []
for i in range(n):
    if(i==min_ind)|(i==max_ind):
        continue
    x,y = xy[i*2:i*2+2]

    nums.append((x,i))
    nums.append((y,i))

nums.append((min_pair,min_ind))
nums.append((max_pair,max_ind))

nums.sort()

set0 = set(range(n))
set1 = set()
set2 = set()

left = 0
right = 0
while(right <= len(nums)):
    if(not set0):
        b = nums[right-1][0] - nums[left][0]
        ans = min(ans,r*b)

        l_ind = nums[left][1]
        if(l_ind in set2):
            set2.remove(l_ind)
            set1.add(l_ind)
        else:
            set1.remove(l_ind)
            set0.add(l_ind)

        left += 1

    else:
        if(right==len(nums)):
            break
        r_ind = nums[right][1]
        if(r_ind in set1):
            set1.remove(r_ind)
            set2.add(r_ind)
        else:
            set0.remove(r_ind)
            set1.add(r_ind)
        right += 1

print(ans)

# print(min_num)
# print(big)
# print(small)

'''
パターンわけがえぐいです。

・最小と最大が同じ袋に入っている
→　小さいグループと大きいグループにわけるだけ。

・最小と最大が違う袋に入っている
→違う色に塗る場合
さっきとおなじだが、最小と最大と同じ袋に入ったボール二つの色が固定なことに注意。

→同じ色に塗る場合
もう一つの色の幅をなるべく狭くしたい。
袋の中で小さい方の最大値と、大きい方の最小値を持ってくる。


'''
