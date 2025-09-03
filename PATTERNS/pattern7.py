# * 
# * *
# *   *
# *     *
# * * * * *
for i in range(1,6):
    for j in range(1,i+1):
        print("*" if j == i or j == 1 or i == 5 else " ",end=" ")
    print() 

#         * 
#    *    *
#   *     *
#  *      *
# *****
print()
for i in range(1,6):
    print("  "*(5-i),end="")
    for j in range(1,i+1):
        print("*" if j == i or j == 1 or i == 5 else " ",end=" ")
    print() 

#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
print()
for i in range(1,6):
    print(" "*(5-i),end=" ")
    for j in range(1,i+1):
        print("*" ,end=" ")        
    print() 

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
print()
for i in range(1,6):
    print("  "*(5-i),end="")
    for j in range(1,i+i):
        print("*",end=" ")       
    print() 


#         *
#       *   *
#     *       *
#   *           *
# * * * * * * * * *
print()
for i in range(1,6):
    print("  "*(5-i),end="")
    for j in range(1,i+i):
        print("*"if j == 1 or j == i+i-1 or i == 5 else " ",end=" ")       
    print() 

#         *
#       * * *
#     *   *   *
#   *     *     *
# * * * * * * * * *
print()
for i in range(1,6):
    print("  "*(5-i),end="")
    for j in range(1,i+i):
        print("*"if j<=i or j == i+i-1 or i == 5 else " ",end=" ")       
    print()