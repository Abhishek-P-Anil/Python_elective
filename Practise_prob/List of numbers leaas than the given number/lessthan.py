n=int(input("Enter the no of values:"))
l=[]
for i in range(n):
    l.append(int(input('Enter the value ')))

num=int(input("Enter the number : "))

li=[]
li=[i for i in l if i < num]
print(li)