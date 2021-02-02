k, x = map(int, input().split())
# k = 1
# x = 20

head = x-(k-1)
tail = x+(k-1)

ans = str(head)
for i in range(head+1,tail+1):
    ans = ans + " " + str(i)

print(ans)
