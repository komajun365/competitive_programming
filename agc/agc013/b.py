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

n,m = map(int,readline().split())
data = list(map(int,read().split()))

links = [set() for _ in range(n+1)]
it = iter(data)
for a,b in zip(it,it):
    links[a].add(b)
    links[b].add(a)

ans = [1]
done = [0] * (n+1)
done[1] = 1
now = 1
while(links[now]):
    i = links[now].pop()
    if(done[i]==1):
        continue
    done[i] = 1
    ans.append(i)
    now = i

ans = ans[::-1]
now = 1
while(links[now]):
    i = links[now].pop()
    if(done[i]==1):
        continue
    done[i] = 1
    ans.append(i)
    now = i
    
print(len(ans))
print(' '.join(map(str,ans)))
