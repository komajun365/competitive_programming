import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n, m = map(int, input().split())
uv = [list(map(int, input().split())) for _ in range(m)]
s,t = map(int, input().split())

before_dict = {}
after_dict = {}
after_3 = {}

for i in range(1,n+1):
    before_dict[i] =[]
    after_dict[i] = []
    after_3[i] = []

for i in range(m):
    u, v = uv[i]
    before_dict[v].append(u)
    after_dict[u].append(v)

for i in range(m):
    u, v = uv[i]
    for j in before_dict[u]:
        for k in after_dict[v]:
            if( j != k):
                after_3[j].append(k)

que = []
que_l = 0

def q_app(num):
    global que
    que.append(num)

def q_pop():
    global que_l
    global que
    que_l += 1
    return que[que_l-1]

q_app(s)

length = [-1] * (n+1)
length[s] = 0

check = True

while(check):
    if((len(que) - que_l) == 0):
        break
    num = q_pop()

    for i in after_3[num]:
        if(length[i] == -1):
            length[i] = length[num] + 1
            q_app(i)

    if(length[t] > -1):
        break

print(length[t])
