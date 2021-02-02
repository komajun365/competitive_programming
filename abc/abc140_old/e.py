n = int(input())
p = list(map(int, input().split()))

ans = 0
for i in range(n-1):
    max1 = max(p[i:(i+2)])
    max2 = min(p[i:(i+2)])
    ans += max2
    for j in range((n-i)-2):
        new = p[i+j+2]
        if max1 < new:
            max2 = max1
            max1 = new
        elif max2 < new:
            max2 = new
        ans += max2

print(ans)
