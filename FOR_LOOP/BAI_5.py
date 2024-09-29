def tinh_giai_thua(n):
   giai_thua = 1
   for i in range(1,n+1):
     giai_thua = giai_thua*i
   return giai_thua
n =int(input("nhập vào n: "))
if n<0:
    print("ko có giai thừa.")
elif n==0:
    print("giai thừa của 0 là 1.")
else:
    print("giai thua cua n là: ",tinh_giai_thua(n))


