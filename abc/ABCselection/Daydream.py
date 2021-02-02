s = input()

flag = True
while(flag):
    if s[0:6] == "eraser":
        s = s.replace("eraser", "", 1)
    elif(s[0:5] == "erase"):
        s = s.replace("erase", "", 1)
    elif(s[0:8] == "dreamera"):
        s = s.replace("dream", "", 1)
    elif(s[0:7] == "dreamer"):
        s = s.replace("dreamer", "", 1)
    elif(s[0:5] == "dream"):
        s = s.replace("dream", "", 1)
    else:
        flag = False


if len(s) == 0:
    print("YES")
else:
    print("NO")
