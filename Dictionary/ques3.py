# Creat a dict of 5 country 
country = {"India":"Delhi","Japan":"Tokyo","USA":"Washington DC","Russia":"Moscow","France":"Paris"}
for i in country.keys():
    if i == "India":
        print(country[i])

# WAP to find min, max of student marks
marks = {"Maths":80,"Science":94,"Physics":91,"English":87,"Hindi":67}
min = min(marks.values()) 
max = max(marks.values())
print("Minimum",min, " & ","Maximum",max,)

# WAP dict 5 employee increse salary of each by 10%
employee = {1:800,2:900,3:1400,4:1000,5:750}
for i in employee:
    employee[i] = employee[i] + (employee[i] * 10)/100
print(employee)

print("\n")
# WAP to print freq of each character in a given string using a dictionary
string = "Mayank Rawat"
freq = dict(enumerate(string))  #USED TO CREATE A DICTIONARY
#   OR     
# freq = {}
# ind = 0
# for i in string:
#     freq[ind] = i
#     ind = ind + 1

x = ""
for i in freq.values():
    if x.count(i) != 1 and i != " ":
        print(i," -- ",str(freq).count(i))
        x = x + i
print(freq)


print("\n")
# WAP to create dict whit no and sq
n = int(input("Enter range: "))
sq = {}
for i in range(1,n+1):
    sq[i] = i * i
print(sq)

# WAP to merge two dict
d1 = {"A":"a","B":"b","D":"d","E":"e"}
d2 = {2:4,5:10,7:49,9:81}
d1.update(d2)
print(d1)

# WAP to chech if dict if empty or not 
d = {}
n = len(d)
if n == 0:
    print("Dictionary is empty")
else:
    print("Not Empty")


# WAP to get sum of all values in dict
dict_sum = {2:4,5:10,7:49,9:81}
sum = 0
for i in dict_sum:
    sum = sum + dict_sum[i]
print("SUM of dict values-",sum)


# Create a nested dict with keys:name ,age,and marks
print("\n DETAILS OF ALL STUDENTS")
student = {"MAYANK":{"Name":"Mayank","Age":20,"marks":{"Maths":87,"Science":98}},"NEHA":{"Name":"Neha","Age":21,"marks":{"Maths":97,"Science":86}},"LOKESH":{"Name":"Lokesh","Age":19,"marks":{"Maths":48,"Science":45}}}
for i in student:
    print(student[i])

# WAP to delete all items od dict
d = {2:4,5:10,7:49,9:81}
d.clear()
print(d)

# MOnths dictionary
months = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
for i in months:
    if i == 4:
        print(months[4])

# WAP to take 5 key value pair from user
d1 = {2:4,5:10,7:49,9:81,4:16}
d2 = {4:8,6:12,7:49}
print("COMMON KEYS-",)
for i in d1:
    for j in d2:
        if i == j:
            print(d1[i],end=" ")    
