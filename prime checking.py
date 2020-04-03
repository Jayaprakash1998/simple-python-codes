x=int(input("Enter a number to check it is prime or not :::"))
for i in range(2,x):
    if x % i == 0:
        print("NOT PRIME")
        break
else:
        print("PRIME")
