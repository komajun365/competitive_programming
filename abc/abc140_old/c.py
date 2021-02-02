n = int(input())
b = list(map(int, input().split()))

b2 = [b[0]]
b2.extend(b)
b.append(b[n-2])

ans = 0
for i in range(n):
    ans += min(b[i],b2[i])

print(ans)
