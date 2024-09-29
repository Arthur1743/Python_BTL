#Write a program to find the factorial (giai thừa) of a given number

# Ask the user to enter a number
number = int(input("Enter a number to find its factorial: "))

# kiem tra neu number < 0
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = 1 # khoi tao bien
    for i in range(1, number + 1):
        result *= i

# In ra
print(f"The factorial of {number} is: {result}")

