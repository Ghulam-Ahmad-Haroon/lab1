'''registration={"ghulam":"1234","musa":"4567","kaka":"zoom"}

s=raw_input("enter your name(ghulam/musa/kaka) :")
password=raw_input("enter password")
flag=False
count=0
while(not flag and count <= 3):
    if(registration[s]!=password):
       print("incorrect password :")
       password = raw_input("re enter password")
       count+=1
       if(int(count)>3):
          print("attempts exceeded!")
    else:
       print("welcome")
       flag=true
