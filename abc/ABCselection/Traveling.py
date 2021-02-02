n = int(input())

t_b = 0
x_b = 0
y_b = 0

flag = True
for i in range(n):
    t_a, x_a, y_a = map(int, input().split())
    distance = abs(x_a - x_b) + abs(y_a - y_b)
    time = t_a- t_b
    if(distance <= time) & ((time - distance)%2 == 0):
        flag = True
    else:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")
