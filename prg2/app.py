print("Simple calculator")

a = float(input("Enter number 1: "))
b = float(input("Enter number 2: "))

print("1. Add\n2. Sub\n3. Mult\n4. Div")
n = int(input("Enter choice: ")) 

if n == 1: 
    print("Sum = ", a+b) 
elif n == 2: 
    print("Diff = ", a-b) 
elif n == 3: 
    print("Product = ", a*b) 
elif n == 4: 
    if b == 0: 
        print("Cant divide by 0")
    else:
        print("Quotient = ", a/b) 
else: 
    print("Invalid choice")

    
    
    