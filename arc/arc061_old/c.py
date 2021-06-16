s = input()

s_len  = len(s)
mul = [1,1,2,4,8,16,32,64,128,256]

ans = 0
for i in range(s_len):
    num = int(s[(s_len-1-i)])

    temp = 0
    for j in range(i+1):
        temp += num*(10**j)*mul[(i-j)]

    ans = ans*2 + temp

print(ans)
