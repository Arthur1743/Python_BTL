#Write a program to find the largest element in a given list of numbers

# Nhap so
numbers = input("Enter numbers separated by spaces: ")

# Chuyen doi tu string sang list number
number_list = [int(num) for num in numbers.split()]

# Khoi ta bien de luu gia tri lon nhat và gia su la phan tu dau tien
largest = number_list[0]
for num in number_list:
    if num > largest:
        largest = num  # Update

# in ra
print("The largest number in the list is:", largest)
