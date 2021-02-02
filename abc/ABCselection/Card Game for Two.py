n = int(input())
a_list = list(map(int, input().split()))

a_list = sorted(a_list)

alice = 0
bob = 0
for i in range(n):
    if i%2==0:
        alice += a_list[n-1-i]
    else:
        bob += a_list[n-1-i]

print(alice-bob)
