import math

while True:
    operator = input("Enter an operator (+, -, *, /, ^, sqrt): ")
    try:
        if operator == "sqrt":
            num1 = float(input("Enter your number: "))
            ans = math.sqrt(num1)
        else:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            if operator == "+":
                ans = num1 + num2
            elif operator == "-":
                ans = num1 - num2
            elif operator == "*":
                ans = num1 * num2
            elif operator == "/":
                ans = num1 / num2
            elif operator == "^":
                ans = num1 ** num2
            else:
                print("Your operator is invalid. Please try again")
                continue
        print(f"The answer is: {ans}")
    except Exception as e:
        print(f"Error: {e}") 