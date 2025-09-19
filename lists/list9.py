# d do dog o og g
a = "dog"
l = list(a)
for i in range(0,len(l)):
    x=""
    for j in range(i,len(l)):
        x = x + l[j]
        print(x,end=" ")


l = "dog"
for i in range(len(l)):
    for j in range(i,len(l)):
        print(l[i:j+1],end=" ")
