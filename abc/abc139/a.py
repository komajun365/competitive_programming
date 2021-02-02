S = input()
T = input()

ans=0
for s,t in zip(S,T):
    ans += (s == t)

print(ans)
