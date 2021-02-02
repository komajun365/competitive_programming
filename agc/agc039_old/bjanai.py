s = input()
k = int(input())

# s='aaaabba'
# k=13

leng = len(s)
if(leng==1):
    print(k//2)
    exit()
elif(leng==2):
    if(s[0]==s[1]):
        print(k)
    else:
        print(0)
    exit()

if(s[:-1]==s[1:]):
    print(leng*k//2)
    exit()

ct_1 = 0
s1 = s
s2 = s+s
for i in range(1,leng):
    if(s1[i-1]==s1[i]):
        s1 = s1[:i] + '?' + s1[i+1:]
        ct_1 += 1

ct_2 = 0
for i in range(1,leng*2):
    if(s2[i-1]==s2[i]):
        s2 = s2[:i] + '?' + s2[i+1:]
        ct_2 += 1

ans = ct_1 + (ct_2 - ct_1)*(k-1)

print(ans)
