def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

if __name__ == "__main__":
    print("=== Temperature Converter (Docker Offline) ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Enter choice (1 or 2): ")
    
    if choice == "1":
        c = float(input("Enter Celsius: "))
        print("Fahrenheit =", c_to_f(c))
    elif choice == "2":
        f = float(input("Enter Fahrenheit: "))
        print("Celsius =", f_to_c(f))
    else:
        print("Invalid choice!")