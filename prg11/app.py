print("Temp Converter")
print("1. C to F")
print("2. F to C ")

n = int(input("Enter your choice: "))
temp = int(input("Enter temp: "))

if n == 1: 
    res = 32 + (9/5 * temp)
else: 
    res = 5/9 * (temp-32) 

print(f"Result: {res}")