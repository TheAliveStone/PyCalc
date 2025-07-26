import math

def calculator():
    # Calculator project
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
def weight_conversion():
    # Weight conversion program
    print("CONVERT YOUR WEIGHT!")
    weight = int(input("Enter your weight (in kilos or pounds): "))
    unit = str(input("Kilos or pounds (type 'kilos' or 'pounds'): "))
    if unit == "kilos":
        ounceChoice = str(input("Do you want to see pounds and ounces? (Y or N): "))
        if ounceChoice == "Y":
            weight = weight / 2.2046226218
            pounds = int(weight)
            ounces = (weight - pounds) * 16
            print(f"You are {weight:.1f} pounds and {ounces:.1f} ounces.")
        elif ounceChoice == "N":
            weight = weight / 2.205
            print(f"You are {weight:.1f} kg. ")
    elif unit == "pounds":
        weight = weight * 2.205
        print(f"You are {weight:.1f} kg. ")
def temperature_conversion():
    # Temperature conversion program
    def c_to_f(c): return (c * 9/5) + 32
    def f_to_c(f): return (f - 32) * 5/9
    def c_to_k(c): return c + 273.15
    def k_to_c(k): return k - 273.15
    def f_to_k(f): return (f - 32) * 5/9 + 273.15
    def k_to_f(k): return (k - 273.15) * 9/5 / 32
    print("CONVERT YOUR TEMPERATURE")
    unit = str(input("Enter the unit of your temperature ('C', 'F' or 'K'): ")).upper()
    temp = int(input("Enter the temperature: "))
    finalUnit = str(input("Enter the unit you want to convert to ('C', 'F' or 'K'): ")).upper()
    if unit == finalUnit:
        print(f"Temperature stays the same: {temp}{finalUnit}")
    elif unit == "C" and finalUnit == "F":
        print(f"Result: {c_to_f(temp):.2f}°F")
    elif unit == "F" and finalUnit == "C":
        print(f"Result: {f_to_c(temp):.2f}°C")
    elif unit == "C" and finalUnit == "K":
        print(f"Result: {c_to_k(temp):.2f}K")
    elif unit == "K" and finalUnit == "C":
        print(f"Result: {k_to_c(temp):.2f}°C")
    else:
        print("This conversion is not implemented yet.")
    
def compound_interest_calculator():
    p = float(input("Enter your starting amount of money: "))
    r = float(input("Enter annual interest rate (as %): ")) / 100
    n = int(input("Number of times interest is compounded per year: "))
    t = float(input("Number of years: "))

    amount = p * (1 + r/n) ** (n*t)
    print(f"After {t:.2f} years, you would have: £{amount:.2f}")

def main():
    print("Select an option:")
    print("1. Calculator")
    print("2. Weight Conversion")
    print("3. Temperature Conversion")
    print("4. Compound Interest Calculator")

    option = input("Enter your choice: ")
    if option == "1":
        calculator()
    elif option == "2":
        weight_conversion()
    elif option == "3":
        temperature_conversion()
    elif option == "4":
        compound_interest_calculator()
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()