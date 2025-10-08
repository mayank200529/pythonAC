# Parameterized and Functional recursion

# Lets take an example to understand this
# WAP to print sum of n natural no.s

# PARAMETERIZED
print("Parametrized recursion sum-")
def func(sum,i,N):
    if i > N:
        print(sum)
        return
    func(sum+i,i+1,N)
func(0,1,10)

# FUNCTIONAL
print("Functonal recursion sum-")
def func(N):
    if N == 1:
        return 1
    return N + func(N-1)
c = func(10)
print(c)