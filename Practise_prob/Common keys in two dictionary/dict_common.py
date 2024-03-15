dict1={}
n=int(input("Enter the number of elements in the dict : "))
for i in range(n):
    key1=input("Enter the key : ")
    value1=input("Enter the value : ")
    dict1[key1]=value1

dict2={}
n=int(input("Enter the number of elements in the dict : "))
for i in range(n):
    key1=input("Enter the key : ")
    value1=input("Enter the value : ")
    dict2[key1]=value1

for key1 in dict1:
    if key1 in dict2:
        print(key1)