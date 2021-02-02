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

def print_ok():
    print('Yes')
    exit()

def print_ng():
    print('No')
    exit()

s = input()
if(len(s)==1):
    if(s=='8'):
        print_ok()
    else:
        print_ng()
elif(len(s)==2):
    a = int(s[0])
    b = int(s[1])
    if((a*10+b)%8==0) or ((a+b*10)%8==0):
        print_ok()
    else:
        print_ng()

cnt = [0] * 10
for i in range(1,10):
    cnt[i] = s.count(str(i))

for x in range(104,1000,8):
    a = x//100
    b = (x%100)//10
    c = x%10
    cnt_x = [0]*10
    for i in [a,b,c]:
        cnt_x[i] += 1
    if(cnt_x[0] > 0):
        continue
    for i in range(1,10):
        if(cnt[i] < cnt_x[i]):
            break
    else:
        print_ok()

print_ng()
