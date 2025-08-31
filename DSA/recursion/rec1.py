# count = 0
# def func():
#     if count == 4:
#         return
#     print("MAYANK")
#     count = count + 1
#     func()
# func()

# count = 0
# def fun():
#     if count == 4:
#         return
#     count = count + 1
#     print("Mayank")
#     fun()
# fun()

# print x < N times using recursion
def func(x,N):
    if N == 0:
        return
    print(x)
    func(x,N-1)
func(15,3)

print()
# print 1 to N using recursion
# this is head recursion
def fun(i,N):
    if i > N:
        return
    print(i)
    fun(i+1,N)
fun(1,4)

print()
# print N to 1 using recursion
# this is tail recursion
def fun(i,N):
    if i > N:
        return
    fun(i+1,N)
    print(i)
fun(1,4)