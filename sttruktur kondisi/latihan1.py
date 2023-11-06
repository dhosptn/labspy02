# Minta pengguna untuk memasukkan dua bilangan
bilangan1 = float(input("Masukkan bilangan pertama: "))
bilangan2 = float(input("Masukkan bilangan kedua: "))

# Gunakan statement if untuk menentukan bilangan terbesar
if bilangan1 > bilangan2:
    terbesar = bilangan1
else:
    terbesar = bilangan2

# Tampilkan bilangan terbesar
print("Bilangan terbesar adalah:", terbesar)
