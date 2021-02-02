n,k = map(int, input().split())
s = input()

bad = 0
for i in range(n-1):
    if s[i] != s[i+1]:
        bad += 1

if bad > k*2:
    ans = (n-1) - bad + (k*2)
else:
    ans = n-1

print(ans)
