n=int(input("How many employee's data do you have:"))
data={}

for _ in range(n):
    name=input("\nEnter name:")
    phno=input("Enter phonr number:")
    data[name]=phno

print("\nData of the employees:")
for name,phno in data.items():
    print("Name:",name,"  Phone number:",phno)