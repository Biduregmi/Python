#PROGRAM TO FIND FACTORIAL USING FOR LOOP
a=int(input("Enter a number:"))
factorial=1
i=1
for i in range(1,a+1):
    factorial*=i
print("Factorial of",a," is:",factorial)   