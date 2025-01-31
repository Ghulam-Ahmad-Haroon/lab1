choice=-1
temp=-1

choice=raw_input("press 1 for celcius or 2 for farenheit :")
if choice==1:
    temp = int(raw_input("enter temp in farenheit :"))
    temp=(temp-32)*(5/9)
    print("C:"+str(temp))
else :
    temp=temp = int(raw_input("enter temp in celcuis :"))
    temp=(9/5)*temp +32
    print("F:"+str(temp))
