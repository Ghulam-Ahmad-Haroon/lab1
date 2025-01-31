'''list=[]
for i in range(0,6):
    while(1):
        try:
            x=int(raw_input("enter number :"))
        except ValueError:
            print("enter valid value!")
        else:
            break
    list.append(x)
print("avg is",sum(list)/len(list))
