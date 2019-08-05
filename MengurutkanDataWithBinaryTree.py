class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
#method untuk membandingkan data dengan parent (dengan konsep binary tree)
    def insert(self, data):
        if self.data:
            if data < self.data: #pertama data di cek dan dimasukan ke kiri jika kosong
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data: #kondisi kedua jika kiri sudah terisi, maka akan masuk ke kanan
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

#method untuk cetak hasil yang dimasukan kedalam binary tree
#dimana hasil yang di cetak dari kiri ke kanan
    def cetak(self):
        if self.left:  
            self.left.cetak()
        print(self.data)
        if self.right:
            self.right.cetak()
            
#tahap eksekusi dimana data dimasukan ke binary tree
tree = Node(80)
tree.insert(9)
tree.insert(5)
tree.insert(2)
tree.insert(8)
tree.insert(1)
print("Hasil dari binary tree : ")
tree.cetak()