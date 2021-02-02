a = int(input())
b = int(input())
c = int(input())
x = int(input())

x = x/50

ans = 0
for a_num in range(a+1):
    for b_num in range(b+1):
        for c_num in range(c+1):
            if (a_num*10 + b_num*2 + c_num) == x:
                ans +=1

print(ans)
