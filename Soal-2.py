phi = float(22/7)
#Untuk  integer
r = int(input("Masukkan Jari\u00b2 Lingkaran = "))
#Untuk float
# r = float(input("Masukkan Jari\u00b2 Lingkaran = "))
luas = phi*r**2
Hasil = (" Luas lingkaran dengan jari-jari {} cm adalah {:.2f} cm\u00b2.") . format(r, luas)
print(Hasil)