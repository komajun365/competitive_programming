n = int(input())

xs = [0]*n
ys = [0]*n

for i in range(n):
    xs[i], ys[i] = map(int, input().split())

max_num = 0
for i in range(n):
    for j in range(i+1,n):
        max_num = max(max_num, ((xs[i]-xs[j])**2 + (ys[i]-ys[j])**2)**(1/2) )

print(max_num)
