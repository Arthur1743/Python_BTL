#Write a program to check if a given number is prime (số nguyên tố)

# Nhap vao so can check
number = int(input("Enter a number to check if it is prime: "))

# Neu so < 2 thi ket luan lun
if number < 2:
    print(f"{number} is not a prime number.")
else:
    is_prime = True  # Gia su la prime
    # Kiem tra tu 2 den can bac 2
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:  # Neu number chia het cho i
            is_prime = False  # Đặt is_prime thành False
            break  # Stop check
    # In kết quả
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
