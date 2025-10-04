student = {"Mayank":{"Name":"Mayank Singh Rawat","Class":"B.TECH","YEAR":"4th","City":"Ajmer","Phone No.":"956484132"},
           "Pal":{"Name":"Pal Chaplot","Class":"B.TECH","YEAR":"3th","City":"Rajsamand","Phone No.":"785464645"},
           "Neha":{"Name":"Neha Dhakar","Class":"B.TECH","YEAR":"4th","City":"Toda","Phone No.":"758184853"},
           "Nishita":{"Name":"Nishita Gupta","Class":"B.TECH","YEAR":"3th","City":"Jaipur","Phone No.":"6898848524"},}

# print(student)
print("\nITEMS")
for i in student.items():
    print(i)

print("\nVALUES")
for i in student.values():
    print(i)

print("\nParticular Person Data(items)")
for i in student:
    if i == "Mayank":
        for j in student[i].items():
            print(j)

print("\nParticular Person Data(value)")
for i in student:
    if i == "Mayank":
        for j in student[i].values():
            print(j,end=" | ")


print("\n\nPrint data whose class is btech")
for i in student:
    if student[i]["Class"] == "B.TECH":
        print(student[i])

print("\nPrint data whose class is btech and city is rajsamnd")
for i in student:
    if student[i]["Class"] == "B.TECH" and student[i]["City"] == "Rajsamand":
        print(student[i])
        print(student[i].values())