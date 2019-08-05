num_array = list() #array dengan N index
num = input("Masukan berapa index array yang diinginkan : ")
print("Masukan angka kedalam array : ")
for i in range(int(num)):
    n = input("Masukan angka : ")
    num_array.append(int(n))
    
#fungsi untuk menentukan angka terkecil pada array
def angka_terkecil(a):
    min_value = None
    for value in a:
        if not min_value:
            min_value = value
        elif value < min_value:
            min_value = value
    return min_value

#fungsi untuk menentukan angka terbesar pada array
def angka_terbesar(b):
    max_value = None
    for value in b:
        if not max_value:
            max_value = value
        elif value > max_value:
            max_value = value
    return max_value

#fungsi untuk menentukan median pada array
def angka_median(lst):
    n = len(lst)
    if n < 1:
        return None
    if n % 2 == 1:
        return sorted(lst)[n//2]
    else:
        return(sorted(lst)[n//2-1:n//2+1])/2.0
    
#fungsi untuk menentukan rata-rata pada array
def angka_rata(l):
    return sum(l, 0.0)/len(l)

#fungsi untuk menentukan standar deviasi pada array
def _ss(data):
    c = angka_rata(data)
    ss = sum((x-c)**2 for x in data)
    return ss

def angka_dev(data, ddof=0):
    n = len(data)
    if n < 2:
        raise ValueError('variance requires at least two data points')
    ss = _ss(data)
    pvar = ss/(n-ddof)
    return pvar**0.5

#fungsi untuk menentukan modulo pada array
def angka_mod(mod):
    return [i % 2 for i in mod]

print("Hasil Perhitungan Statistika dengan Python")
print("Array yang kamu input          : ", num_array)
print("Angka yang paling kecil adalah : ", angka_terkecil(num_array))
print("Angka yang paling besar adalah : ", angka_terbesar(num_array))
print("Mediannya adalah               : ", angka_median(num_array))
print("Rata-ratanya adalah            : ", angka_rata(num_array))
print("Standar Deviasinya adalah      : ", angka_dev(num_array, ddof=1))
print("Modulonya adalah               : ", angka_mod(num_array))