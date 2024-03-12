dict1={}
n=int(input("Enter the number of elements in the dict : "))
for i in range(n):
    key1=input("Enter the key : ")
    value1=input("Enter the value : ")
    dict1[key1]=value1

dict2={}
for key1 in dict1:
    value1=dict1[key1]
    dict2[value1]=key1

print("Dict1 = ",dict1)
print("Dict2 = ",dict2)