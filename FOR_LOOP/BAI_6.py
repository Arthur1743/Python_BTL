def so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
n = int(input(" nhap so tu nhien: "))
if so_nguyen_to(n):
    print(f"{n} la so nguyen to")
else:
    print(f"{n} khong phai so nguyen to")
