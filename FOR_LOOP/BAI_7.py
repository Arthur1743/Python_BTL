def dao_nguoc_so(n):
  so_dao_nguoc = 0
  for i in range(len(str(n))):
    chu_so = n % 10
    so_dao_nguoc = so_dao_nguoc * 10 + chu_so
    n //= 10
  return so_dao_nguoc
n = int(input(" nhap so tu nhien: "))
t = dao_nguoc_so(n)
print("Số đảo của", n, "là:", t)



