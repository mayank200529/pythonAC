# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

for i in range(1,6):
    for j in range(1,6):
        print("* ",end=" ")
    print()

print()
# * & * & * 
# * & * & * 
# * & * & * 
# * & * & * 
# * & * & * 

for i in range(1,6):
    for j in range(1,6):
        print("& " if j % 2 == 0 else "* ",end = " ")
    print()
    
print()
# * * * * * 
# & & & & &
# * * * * *
# & & & & &
# * * * * *
for i in range(1,6):
    for j in range(1,6):
        print("* " if i % 2 == 1 else "& ",end=" ") 
    print()
    
print()
# 1 2 3 4 5 
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ") 
    print()             

print()
# 1 1 1 1 1 
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5
for i in range(1,6):
    for j in range(1,6):
        print(i,end=" ") 
    print()             

