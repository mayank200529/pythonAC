#WAP to ask the user to enter names of thier 3 favourite movies & store them in a list.
a = input("enter the first favorite movie:")
b = input("enter the second favorite movie:")
c = input("enter the third favorite movie:")
list = [a,b,c]
print(list) 
#or 
movies = []
mov1 = input("enter the first favorite movie:")
mov2 = input("enter the second favorite movie:")
mov3 = input("enter the third favorite movie:")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)
#or
movies = []
movies.append(input("enter 1st movie:"))
movies.append(input("enter 2nd movie:"))
movies.append(input("enter 3rd movie:"))
print(movies)   