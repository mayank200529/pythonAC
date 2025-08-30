# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
"""
# methord 1
for i in range(5):
    print("* "* 5)

# methord 2
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()
"""

# * * * * * *
# *         *
# * * * * * *
# *         *
# * * * * * *

# for i in range(1,6):
#     print("* * * * * *" if i % 2 == 1 else = "*       *")

# for i in range(1,6):
#     for j in range(1,6):
#         print("* " if i % 2 == 1 or j % 2 == 1 else " ",end="")


for i in range(1,6):
    # for j in range(1,6):
    print(chr(64 + i) * 5)

    print()