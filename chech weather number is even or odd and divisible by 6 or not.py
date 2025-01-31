a=int(input("Enter a integer:"))

if(a%2==0):
    if(a%6==0):
        print(a," is a even number and it is divisible by 6.")
    else:
        print(a," is a even number and it is not divisible by 6.")
else:
    print(a," is a odd number hence it is not divisible by 6.")
