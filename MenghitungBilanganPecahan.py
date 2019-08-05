print("Program Menghitung Bilangan Pecahan dengan Python")
print("1. Penjumlahan \n2. Pengurangan \n3. Perkalian \n4. Pembagian")

pilih = input("Masukan pilihan operasi bilangan [1-4] : ")

#inputan bilangan pecahan
b1 = input("Masukan bilangan bulat pertama : ")
pm1 = input("Masukan bilangan pembilang pertama : ")
p1 = input("Masukan bilangan penyebut pertama : ")
b2 = input("Masukan bilangan bulat kedua : ")
pm2 = input("Masukan bilangan pembilang kedua : ")
py2 = input("Masukan bilangan penyebut kedua : ")

#konversi inputan dari string ke integer
int_b1 = int(b1)
int_pm1 = int(pm1)
int_p1 = int(p1)
int_b2 = int(b2)
int_pm2 = int(pm2)
int_py2 = int(py2)

print("Kedua pecahan bilangan yang dimasukan")
print(" ", int_pm1, " ", " ", " ", " ", int_pm2, " ")
print(int_b1, "-", " DAN ", int_b2, "-", " ")
print(" ", int_p1, " ", " "," ", " ", int_py2, " ")
print(" ")

#switch case versi python dengan menggunakan if sebagai alternatif
#jika kondisi equal dengan inputan 1-4
if pilih == "1": #pertambahan pecahan 
    int_pm1 = (int_p1 * int_b1) + int_pm1 #Perhitungan untuk penyederhanaan pecahan
    int_pm2 = (int_py2 * int_b2) + int_pm2 #Perhitungan untuk penyederhanaan pecahan
    print("Hasil penyederhanaan pecahan tanpa bilangan bulat")
    print(int_pm1, " ", int_pm2)
    print("-", "+", "-")
    print(int_p1, " ", int_py2)
    print(" ")
    py = int_p1 * int_py2
    int_pm1 = (py / int_p1) * int_pm1
    int_pm2 = (py / int_py2) * int_pm2
    pm = int_pm1 + int_pm2
    print("Hasil perhitungannya adalah : ")
    print(int(int_pm1), " ", int(int_pm2), " ", int(pm))
    print("-", "+", "-", "=", "-")
    print(py, " ", py, " ", py)
if pilih == "2": #pengurangan pecahan
    int_pm1 = (int_p1 * int_b1) + int_pm1 #Perhitungan untuk penyederhanaan pecahan
    int_pm2 = (int_py2 * int_b2) + int_pm2 #Perhitungan untuk penyederhanaan pecahan
    print("Hasil penyederhanaan pecahan tanpa bilangan bulat")
    print(int_pm1, " ", int_pm2)
    print("-", "-", "-")
    print(int_p1, " ", int_py2)
    print(" ")
    py = int_p1 * int_py2
    int_pm1 = (py / int_p1) * int_pm1
    int_pm2 = (py / int_py2) * int_pm2
    pm = int_pm1 - int_pm2
    print("Hasil perhitungannya adalah : ")
    print(int(int_pm1), " ", int(int_pm2), " ", int(pm))
    print("-", "X", "-", "=", "-")
    print(py, " ", py, " ", py)
if pilih == "3": #perkalian pecahan
    int_pm1 = (int_p1 * int_b1) + int_pm1 #Perhitungan untuk penyederhanaan pecahan
    int_pm2 = (int_py2 * int_b2) + int_pm2 #Perhitungan untuk penyederhanaan pecahan
    print("Hasil penyederhanaan pecahan tanpa bilangan bulat")
    print(int_pm1, " ", int_pm2)
    print("-", "X", "-")
    print(int_p1, " ", int_py2)
    print(" ")
    py = int_p1 * int_py2
    int_pm1 = (py / int_p1) * int_pm1
    int_pm2 = (py / int_py2) * int_pm2
    pm = int_pm1 * int_pm2
    print("Hasil perhitungannya adalah : ")
    print(int(int_pm1), " ", int(int_pm2), " ", int(pm))
    print("-", "X", "-", "=", "-")
    print(py, " ", py, " ", py)
if pilih == "4": #pembagian pecahan
    int_pm1 = (int_p1 * int_b1) + int_pm1 #Perhitungan untuk penyederhanaan pecahan
    int_pm2 = (int_py2 * int_b2) + int_pm2 #Perhitungan untuk penyederhanaan pecahan
    print("Hasil penyederhanaan pecahan tanpa bilangan bulat")
    print(int_pm1, " ", int_pm2)
    print("-", ":", "-")
    print(int_p1, " ", int_py2)
    print(" ")
    pm = int_pm1 * int_py2
    py = int_p1 * int_pm2
    print("Hasil perhitungannya adalah : ")
    print(int(int_pm1), " ", int(int_py2), " ", int(pm))
    print("-", ":", "-", "=", "-")
    print(py, " ", py, " ", py)
else:
    print("Pilihan salah, pastikan anda memasukan pilihan angka 1-4")