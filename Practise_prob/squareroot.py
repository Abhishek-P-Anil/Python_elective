num = int(input("Enter a positive number : "))
pyth_est = num**(1/2)
z=1
while ("%0.5f" % z != "%0.5f" % pyth_est):
    z=(z+num/z)/2
print("The program's estimate : ",z,"\nPython's estimate ",pyth_est)
