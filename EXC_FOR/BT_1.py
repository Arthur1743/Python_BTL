#Prints all even numbers between 1 and N and calculates their sum

# Nhap gia tri n
N = int(input("Enter the value of N: "))

# Khoi tao bien tong
even_sum = 0

# In va tinh tong
print("Even numbers between 1 and", N, "are:")
for i in range(2, N + 1, 2):  # Bat dau tu 2, step la 2
    print(i, end=" ")
    even_sum += i

# In tổng các số chẵn
print("\nSum of even numbers:", even_sum)
