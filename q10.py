'''def is_prime(x):
    count = 0
    for i in range(1,x/2+1):
        if(x%i==0):
            count+=1
            if(count>1):
                return False
    return True


x=input("enter number :")
if(x==0):
    print("neither prime nor composite")
elif(x==1):
    print("False")
else:
    print(is_prime(x))