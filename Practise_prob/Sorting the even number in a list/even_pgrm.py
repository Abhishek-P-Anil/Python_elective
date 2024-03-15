n=int(input("Enter the no of values:"))
l=[]
for i in range(n):
    l.append(int(input('Enter the value ')))


li=[]
li=[i for i in l if i%2==0]
li.sort()
print(li)