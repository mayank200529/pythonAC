# # s = input("Enter a string-")

# s = "Heello my naaame is maayank and my freind name is lokesh"
# l = list(s)
# i = 0
# while i<len(l):
#     if l[i] in ["A","E","I","O","U","a","e","i","o","u"]:
#         l.pop(i)
#         i = i - 1
#     else:
#         i += 1
# l = "".join(l)
# print(l)



# s = "Hello my name is mayank and my freind name is lokesh"
# s = s.lower()
# l = s.split(" ")
# print()
# for i in range(len(l)):
#     if i%2==0:
#         l[i]=l[i].upper()
# s = " ".join(l)
# print(s)


# # print()
# # s = "Mayank"
# # y = "Hello Word"
# # s = y + " " + s + " " + y
# # print(s)


# print()
# s = "Hello my name is mayank and my freind name is lokesh"
# l = s.split()
# l.append("Hello world")
# l.insert(0,"Hello World")
# l = " ".join(l)
# print(l)

s = "Hello my name is mayank and my freind name is lokesh"
s = s.split()
i = 0 
n = int(input("Enter how many words to put at last-"))
while i<n:
    t = s[0]
    s.append(t)
    s.pop(0)
    i = i+1
s = " ".join(s)
print(s)
