n,q = map(int, input().split())

boss = {}
point = [0] * n
for i in range(1,n):
    a,b = map(int, input().split())
    boss[b] = a

for i in range(q):
    p,x = map(int, input().split())
    point[p-1] += x

for i in range(2,n+1):
    print("===")
    print(point[i-1])
    print(boss[i])
    print(point[boss[i]])
    point[i-1] += point[boss[i]]
    print(point[i-1])

print(boss)
print(" ".join(map(str,point)))

print(point[0])
