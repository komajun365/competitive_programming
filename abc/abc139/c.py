n = int(input())
h = list(map(int,input().split()))

high = h[0]
now = 0
max = 0

for r_h in h[1:]:
    if(r_h <= high):
        now += 1
    elif( now > max):
        max = now*1
        now = 0
    else:
        now = 0
    high = r_h*1

if(now > max):
    max = now*1

print(max)
