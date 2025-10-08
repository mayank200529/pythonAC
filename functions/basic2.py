# LAMBDA FUNCTION (Used to manage single line functions)
a = 2
p = 10
pw = lambda a,p:a**p
print(pw(a,p))


# Global Arguements
a = 100       #GLOBAL VARIABLE
def show():
    a = 200   #LOCAL VARIABLE
    print(a)
show()
print(a)


a = 100       #GLOBAL VARIABLE
def show():
    global a
    a = 200   #LOCAL Converted into GLOBAL VARIABLE
    print(a)
show()
print(a)