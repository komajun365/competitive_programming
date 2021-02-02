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

n,m = map(int, readline().split())
uvs = list(map(int,read().split()))

links = [dict() for _ in range(n+1)]
it = iter(uvs)
for u,v,s in zip(it,it,it):
    links[u][v] = s
    links[v][u] = s

def dfs(root, init):
    nums = [0] * (n+1)
    depth = [-1] * (n+1)
    parent = [-1] * (n+1)

    nums[root] = init
    depth[root] = 0
    stack = [root]
    while(stack):
        next = []
        while(stack):
            i = stack.pop()
            for j,s_ij in links[i].items():
                if(j == parent[i]):
                    continue

                num_j = s_ij - nums[i]
                if(depth[j] != -1)&(nums[j] != num_j):
                    loop_len = depth[j] + depth[i] + 1
                    if(loop_len%2 == 0):
                        print(0)
                        exit()
                    else:
                        num_j = nums[j] + num_j
                        if(num_j % 2 ==1):
                            print(0)
                            exit()
                        return (False, nums,depth,j,num_j//2)
                elif(depth[j] == -1):
                    depth[j] = depth[i] + 1
                    nums[j] = num_j
                    parent[j] = i
                    next.append(j)
        stack = next[::]

    return(True, nums,depth,0,0)

flag,nums,depth,root,init = dfs(1,0)

if(flag==False):
    flag2,nums,depth,root,init = dfs(root,init)
    if(flag2==False):
        print(0)
    else:
        if(min(nums[1:]) < 1):
            print(0)
        else:
            print(1)
    exit()

even = []
odd = []
for i in range(1,n+1):
    if(depth[i]%2==0):
        even.append(nums[i])
    else:
        odd.append(nums[i])

min0 = min(even)
min1 = min(odd)

ans = 1 + (min0-1) + (min1-1)
print(max(0,ans))


'''
・n = m+1
→　二部グラフなので、適当に作ってそれぞれのグラフの部集合について、最小値と最大値から計算

・それ以外
→　絶対にどこかに閉路がある。

・偶数長の閉路
→　適当に作って一致すればいいが、一致しないならどうやってもダメ。

・奇数長の閉路
→　うまく作れば1通りだけうまくいく可能性がある。

・閉路は偶数長か、奇数長か？
→　根からの距離を合計すれば判定できる。
→　一致しなくて偶数長　→　無理
　一致しなくて奇数長　→　値を調整して再チャレンジ。最後まで作り切れれば答えは1

'''
