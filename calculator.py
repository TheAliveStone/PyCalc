import math

operator = input("Enter an operator (+, -, *, /, ^, sqrt): ")
if operator == "sqrt":
    num1 = int(input("Enter your first number: "))
else:
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your twice number: "))
ans = 0

if operator == "+":
    ans = num1 + num2
elif operator == "-":
    ans = num2 - num1
elif operator == "*":
    ans = num1 * num2
elif operator == "/":
    ans = num1 / num2
elif operator == "^":
    ans = num1 ^ num2
elif operator == "sqrt":
    ans = math.sqrt(num1)