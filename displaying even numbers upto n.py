#To print the even numbers between 1 to n number entered by user.
n=int(input("Enter a number:"))
print("The even numbers between 0 to",n," are:")
for a in range(1,n+1):
    if(a%2 !=0):
        continue
    print(a)