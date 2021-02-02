n = int(input())
x = int(input(), 2)

def do_step(i,n):
    if(i&1 == 1):
        i = i >> 1
    else:
        i = i >> 1
        i += 2**(n-1)
    return(i)

mod_n = 998244353
ans = (((x+1)%mod_n) * 2 * n)%mod_n

for i in range(3,n+1,2):
    if(n % i == 0):
        temp = ''
        for j in range(i):
            if(j%2==0):
                temp = temp + '0'*(n//i)
            else:
                temp = temp + '1'*(n//i)
        temp = int(temp,2)
        # print(temp)

        root = []
        first = temp
        root.append(temp)
        flag = True
        while(flag):
            temp = do_step(temp,n)
            if(temp==first):
                flag=False
            else:
                root.append(temp)

        print(root)
        for j in root:
            if(j <= x):
                ans -= 2*n
                ans += (2*n)//i

ans = ans%mod_n

print(ans)


==========
n=30
int('001110011011011101010111011100',2) * 2 * n % mod_n

n=15
temp = int('000101110100010', 2)

root = []
first = temp
root.append(temp)
flag = True
while(flag):
    temp = do_step(temp,n)
    if(temp==first):
        flag=False
    else:
        root.append(temp)

print(root)
