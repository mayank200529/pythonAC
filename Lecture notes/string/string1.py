a = "Mayank"
b = 'String is immutable in pythons'
c = '''Mayank Singh
        Rawat'''
print(a)
print(a[0]+a[5])
# a[0]= "p" #It is not possible immutablity
print(b)
print(c)

d = "In string all character are stored in indexes "
print(d)

for i in a :
    print(i,end=" ")
print()
for i in range(0,len(a)):
    print(a[i],end=" ")
print()
for i in range(len(a)-1,-1,-1):
    print(a[i],end=" ")


print(a[:])
print(a[2:])
print(a[:4])
print(a[::2])
print(a[-1])
print(a[-1::-1])