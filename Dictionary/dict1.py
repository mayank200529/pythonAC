# 
d = {"AII":"AJMER","JP":"JAIPUR","UDZ":"UDAPIUR"}
d = {0:"MAYANK",1:"PAL",2:"NISHITA",3:"NEHA"}
d = {0:[1,2,3,4,5,6],1:[6,5,9,8,7,2]}
d = {0:{1,2,3,4,5,6},1:{6,5,9,8,7,2}}
print(type(d))


# How to access dictionary
d = {"AII":"AJMER","JP":"JAIPUR","UDZ":"UDAPIUR"}
print(d["AII"])
print(d.get("JP"))

for x in d:
    print(x, "=>", d[x])
    # x is for keys
    # d[x] is for data

print("\nITEMS-")
for x in d.items():
    print(x)
print("\nKEYS-")
for x in d.keys():
    print(x)
print("\nVALUES-")
for x in d.values():
    print(x)


print("\nPOP FUNCTION")
d.pop("JP")
print(d)

print("\nPOP ITEM FUNCTION")
d.popitem()
print(d)

print("\nCLEAR FUNCTION")
d.clear()
print(d)

print("\nUPDATE FUNCTION")
d.update({"BK":"BIKANER","JP":"JAIPUR"})
print(d)

print("\nCOPY FUNCTION")
d.copy()
print(d)

print("\nFROMKEYS FUNCTION")
d = d.fromkeys(["MK","LO","NE"],"")
print(d)
d["MK"] = "MAYANK"
d["LO"] = "LOKESH"
d["NE"] = "NEHA"
print(d)

print("\nDELETE FUNCTION")
del d["LO"] 
# for deleting whole dict =>> del d
print(d)

