inv = int(input("Enter the investment amount : "))
time = int(input("Enter the number of years : "))
rate = int(input("Enter the rate as a %: "))
bal = inv
print("Year\tStarting balance\tInterest\tEnding balance")
for i in range (1,time+1):
    print("  ",i,"\t","%0.2f" % bal,"\t\t", end="")
    interest = (bal*rate)/100
    bal = bal + interest
    print(" ","%0.2f" % interest ,"\t", "%0.2f" % bal)
print("Ending balance : $","%0.2f" % bal)
print("Total interest earned : $","%0.2f" % (bal-inv))

