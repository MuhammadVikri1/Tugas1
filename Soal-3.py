Teori = float(input("\nMasukkan nilai Teori: "))
Praktek = float(input("Masukkan nilai Praktek: "))
if Teori >= 70 and Praktek >= 70:
    print ("Selamat Anda lulus!")
elif Teori >= 70 and Praktek < 70:
    print ("Anda Harus Mengulang Ujian Praktek")
elif Teori < 70 and Praktek >= 70:
    print ("Anda Harus Mengulang Ujian Teori")
elif Teori < 70 and Praktek < 70:
    print ("Anda Harus Mengulang Ujian Teori dan Praktek")

