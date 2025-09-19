s = "Hello my name is mayank and my freind name is lokesh"
s = s.lower()
l = list(s)
# Hello My Name Is Mayank And My Freind Name Is Lokesh
for i in range(len(l)):
    if i == 0 or l[i-1]==" " :
        l[i] = l[i].upper()
s = "".join(l)
print(s)

s = "Hello my name is mayank and my freind name is lokesh"
s = s.lower()
l = list(s)
print()
# OUTPUT - hellO mY namE iS mayanK anD mY freinD namE iS lokesH
for i in range(len(l)):
    if l[i]==" " :
        l[i-1] = l[i-1].upper()
    l[len(l)-1] = l[len(l)-1].upper()
s = "".join(l)
print(s)

s = "Hello my name is mayank and my freind name is lokesh"
s = s.lower()
l = list(s)
print()
# HellO MY NamE IS MayanK AnD MY FreinD NamE IS LokesH
for i in range(len(l)):
    if l[i]==" ":
        l[i-1] = l[i-1].upper()
        l[i+1] = l[i+1].upper()
    l[0] = l[0].upper()
    l[len(l)-1] = l[len(l)-1].upper()
s = "".join(l)
print(s)


s = "Hello my name is mayank and my freind name is lokesh"
s = s.lower()
l = list(s)
print()
# OUTPUT - HeLlO My nAmE Is mAyAnK AnD My fReInD NaMe iS LoKeSh
for i in range(len(l)):
    if i%2==0:
        l[i]=l[i].upper()
s = "".join(l)
print(s)


s = "Hello my name is mayank and my freind name is lokesh"
s = s.lower()
l = s.split(" ")
print()
# OUTPUT - HELLO my NAME is MAYANK and MY freind NAME is LOKESH 
for i in range(len(l)):
    if i%2==0:
        l[i]=l[i].upper()
s = " ".join(l)
print(s)


s = "Hello my name is mayank and my freind name is lokesh"
s = s.upper()
l = list(s)
print()
# OUTPUT - HELLO my NAME is MAYANK and MY freind NAME is LOKESH 
for i in range(len(l)):
    if i==0 or l[i-1] == " " or  i==len(l)-1 or l[i+1] == " " :
        l[i]=l[i].lower()
s = "".join(l)
print(s)


s = "Hello my name is mayank and my freind name is lokesh"
s = s.upper()
l  = s.split(" ")
print()
for i in range(len(l)):
    x = list(l[i])
    x = "".join(x[-1::-1])
    print(x,end=" ")