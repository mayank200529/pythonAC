#WAP TO check if a list contains palindrome of elements.(hint:use copy() method)
list1 = [1,2,3,2,1]
copy_list1 = list1.copy()
copy_list1.reverse()
if(list1==copy_list1):
    print("It is palindrome of element")
else:
    print("not palindrome")