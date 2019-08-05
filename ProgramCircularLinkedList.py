class Node :
    #inisialisasi Node
    def __init__(self, data):
        self.data = data
        self.next = None
        
class CircularLinkedList :
    
    def __init__(self):
        self.head = None
        
        
    def push(self, data):
        ptr1 = Node(data)
        temp = self.head
        
        ptr1.next = self.head
        
        if self.head is not None:
            while (temp.next != self.head):
                temp = temp.next
            temp.next = ptr1
        else:
            ptr1.next = ptr1
        self.head = ptr1
    
    def cetak(self):
        temp = self.head
        if self.head is not None:
            while (True):
                print(temp.data, end=' ')
                temp = temp.next
                if (temp == self.head):
                    break

#eksekusi program
#insialisasi list
listcircular = CircularLinkedList()

#memasukan data kedalam list
listcircular.push(9)
listcircular.push(1)
listcircular.push(2)
listcircular.push(4)
listcircular.push(6)
print("Hasil dari Circular Linked List : ", end=' ')
listcircular.cetak()
print(" ")