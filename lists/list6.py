s = "Hello my name is mayank and my freind name is lokesh"

# print string in reverse
l = s.split(" ") 
l.reverse()
s = " ".join(l)
print(s)


# print every word in reverse
# methord 1
print()
l  = s.split(" ")
for i in range(len(l)):
    x = list(l[i])
    x = "".join(x[-1::-1])
    print(x,end=" ")

# methord 2
print()
l  = s.split(" ")
for i in range(len(l)):
    x = list(l[i])
    x.reverse()
    x = "".join(x)
    print(x,end=" ")

# juggad not to be used
print()
l  = s.split(" ")
print(l)
for i in l:
    print(i[-1::-1],end=" ")

