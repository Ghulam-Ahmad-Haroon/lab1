'''list=[1,1,2,3,4,5,4,5,6,6,7,6]
i=0
j=0
while(i<len(list)-1):
   j=i+1
   while(j<len(list)):
        if(list[i]==list[j]):
            list.pop(j)
        else:
            j+=1
   i+=1

print(list)

