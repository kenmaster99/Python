class Node :
    
    def __init__(self, data): #inisialisasi node
        self.data = data
        self.next = None
        
class linkedlist :

    def __init__(self):
        self.head = None
    
    def tampil(self):
        current = self.head
        while current is not None: #looping
            print(' ', current.data, end=' ')
            current = current.next
    
    def insert(self, new_data): #method print data yang dimasukan
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node
        
    def sortir(self) : #method untuk sortir dengan double linked list
        current =self.head
        index = None
        if(self.head == None):
            return
        else:
            while(current != None):
                index = current.next
                while(index != None):
                    if (current.data > index.data):
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next
                
#eksekus program dengan memasukan data kedalam list
#pertama inisialisasi list terlebih dahulu
linkedlist1 = linkedlist()
#selanjutnya masukan beberapa data yang diinginkan
linkedlist1.insert(8)
linkedlist1.insert(3)
linkedlist1.insert(6)
linkedlist1.insert(17)
linkedlist1.insert(1)

#tampilkan data yang sudah dimasukan (sebelum di urutkan)
print("Program Sederhana untuk Mengurutkan Data dengan Menggunakan Double Linked List")
print("Sebelum data diurutkan : ", end=' ')
linkedlist1.tampil()
print(' ')
#tampilkan data yang sudah dimasukan (sesudah di urutkan)
print("Sesudah data diurutkan : ", end=' ')
linkedlist1.sortir()
linkedlist1.tampil()