'''def is_pal(s):
    start=0
    end=len(s)-1
    while(start<end):
        if(s[start]!=s[end]):
            return False
        start+=1
        end-=1
    return True

s=raw_input("enter string :")
print(is_pal(s))
