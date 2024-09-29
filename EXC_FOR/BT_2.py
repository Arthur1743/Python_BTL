#Write a program to find the sum of all numbers divisible by 3 or 5 between 1 and N

# Nhap n
N = int(input("Enter the value of N: "))

# khoi tao bien tong
total_sum = 0

for i in range(1, N + 1):
    # Kiem tra neu chia het cho 3 hoac 5
    if i % 3 == 0 or i % 5 == 0:
        total_sum += i

# In ra
print("The sum of all numbers divisible by 3 or 5 between 1 and", N, "is:", total_sum)
