def sortir(data):
    for index in range(1, len(data)):
        current = data[index]
        i = index
        while current < data[i - 1] and i > 0:
            data[i] = data[i - 1]
            i = i - 1
        data[i] = current
        
#eksekusi program
masuk = int(input("Masukan banyaknya index yang diinginkan : "))
data_msk = [int(input()) for i in range (masuk)]
print("Berikut hasil data sebelum di sortir dengan Insertion : ", end=' ')
print(data_msk)
sortir(data_msk)
print("Berikut hasil data sebelum di sortir dengan Insertion : ", end=' ')
print(data_msk)
