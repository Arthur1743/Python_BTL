#Write a program to calculate the sum of all digits in a given number

# Nhap so
number = input("Enter a number: ")

# Khoi tao bien tong
digit_sum = 0
for digit in number:
    if digit.isdigit():  # Check if the character is a digit
        digit_sum += int(digit)  # chuyen sang integer va cong

# in ra
print("The sum of all digits in the number is:", digit_sum)
