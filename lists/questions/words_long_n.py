# Get and print the list of words in a list that are longer than n characters.

l = ["Mayank","Pal","Nishita","Neha","Mukul","Lokesh"]
n = int(input("Enter value of n(min character len)-"))
for i in range(len(l)):
    if len(l[i]) > n:
        print(l[i])
    # else:
    #     print(f"No word with length {n}")
    