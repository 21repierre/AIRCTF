

flag = "f4c9sha2"

u =[]
v=[]
for i in range(0, len(flag), 2):
    u.append(ord(flag[i]) * ord(flag[i+1]))
    v.append(ord(flag[i]) + ord(flag[i+1]))

print(u,v)
for i in range(0, len(flag)):
    print(ord(flag[i]))