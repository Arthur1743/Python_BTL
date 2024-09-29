x = int(input('nhap so x:'))
tong=0
for i in range (1,x+1):
    if i % 3 == 0 or i % 5 == 0 :
        tong = tong +i
print("tong các so chia het cho 3 or 5 tu 1 den ",x,"la:",tong)