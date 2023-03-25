try:
    a  = int(input("Enter the first number: "))
    operation = str(input("enter a sign to perform operation: "))
    b  = int(input("Enter the second number: "))

    if  operation == "+":
        a + b
        print(f"The sum of {a} plus {b} is equal to {a + b}")
        
    elif operation == "-":
        a - b
        print(f"The difference of {a} minus {b} is equal to {a - b}")
        
    elif operation == "/":
        try:
            a / b
            if a < b:
                a, b = b, a
        except ZeroDivisionError:
            exit("Zero is not divisible.")
            
        print(f" {a} divided by {b} is equal to {a / b}")
        
    elif operation == "*":
        a * b
        print(f"The product of {a} multiply by {b} is equal to {a * b}")

    elif operation == "%":
        a % b == 0
        print(f"The remainder of {a} and {b} is {a}")
    else:
        print("Please enter a valid arithmetic.")
except ValueError:
    exit("Please enter a real (integer) number.")
