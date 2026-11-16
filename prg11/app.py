print("Temp Converter")
print("1. C to f ")
print("2. F to C ")
n = int(input("Enter Choice: "))
temp = int(input("Enter temp: "))
if n ==1: 
    res = 32 + (9/5 * temp) 
else: 
    res = 32 - (5/9 * temp)
print(f"Res is : {res}")