
data = [
    [101,"Mayank Rawat","Ajmer","B.TECH"],
    [104,"Pal Chaplot","Rajsamnd","B.TECH"],
    [103,"Neha Dhakar","Tonk","B.TECH"],
    [102,"Lokesh Saini","Village","B.TECH"],
]


# Mayank Rawat
# Pal Chaplot
# Neha Dhakar
# Lokesh Saini
for i in data:
    print(i[1])

# Mayank Rawat B.TECH
# Pal Chaplot B.TECH
# Neha Dhakar B.TECH
# Lokesh Saini B.TECH
for i in data:
    print(i[1], i[3])

# Mayank
# Pal
# Neha
# Lokesh
for i in data:
    print(i[1].split()[0] )

# Rawat
# Chaplot
# Dhakar
# Saini
for i in data:
    print(i[1].split()[1])

# Pal Chaplot
for i in data:
    if str(i[1]).startswith("P"):
        print(i[1])

# Mayank
# Lokesh
for i in data:
    if len(i[1].split()[0])==6:
        print(i[1].split()[0])

# Dhakar
for i in data:
    if len(i[1].split()[1])==6:
        print(i[1].split()[1])