def tinh_tong_chu_so(n):
  tong = 0
  for chu_so in str(abs(n)):
    tong = tong + int(chu_so)
  return tong
n = int(input('nhap so n:'))
print("Tổng các chữ số của n là:",tinh_tong_chu_so(n))






