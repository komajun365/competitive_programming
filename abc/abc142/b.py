n,k = map(int, input().split())
h_list = list(map(int, input().split()))

ans = 0
for h in h_list:
    if(h >= k):
        ans += 1

print(ans)
