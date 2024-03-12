x=input("Enter the string : ")
words=0
if len(x) > 0:
    words=1
    for i in x:
        if (i==" "):
            words=words+1

print("freq of words = ",words)



        