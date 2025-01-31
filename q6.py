'''list1=[]
list2=[]
print("List1")
for i in range(0,5):
    x=raw_input("enter value :"+ str(i+1))
    list1.append(x)
print("List2")
for i in range(0, 5):
    x = raw_input("enter value :" + str(i + 1))
    list2.append(x)
print(list1)
print(list2)
list1=set(list1)
list2=set(list2)
print("intersection")
print(list1.intersection(list2))
print("union")
print(list1.union(list2))
print("difference")
print(list1.difference(list2))
