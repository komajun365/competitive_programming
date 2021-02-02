n,q = map(int, input().split())

boss = {}
point = {}
point[n] = 0
for i in range(1,n):
    a,b = map(int, input().split())
    boss[b] = a
    point[i] = 0

for i in range(q):
    p,x = map(int, input().split())
    point[p] += x

ans = str(point[1])
for i in range(2,n+1):
    point[i] += point[boss[i]]
    ans = ans + " " + str(point[i])

print(ans)
