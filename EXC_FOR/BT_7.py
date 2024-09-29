#Write a program to find the reverse of a given number

# Nhap so
number = input("Enter a number to reverse: ")

# Khoi tao bien
reversed_number = ""

# Bat dau vong lap
for digit in number:
    reversed_number = digit + reversed_number

# In ra
print("The reverse of the number is:", reversed_number)
