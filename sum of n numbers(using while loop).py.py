#Sum of n numbers entered by user
sum=0.00
i=0
a=int(input("How many numbers do you have:"))
print("Enter the numbers:")
while i!=a:
    b=float(input())
    sum +=b
    i+=1
print("The sum of numbers is:",sum)