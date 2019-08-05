class Node :
    def __init__(self, data):
        self.data = data
        self.next = None
        
class linkedlist :
    def __init__(self):
        self.head = None
        
    def insert(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        
        last.next = new_node
        
    def tampilkan_data(self):
        current = self.head
        while current is not None:
            print(' ', current.data, end=" ")
            current = current.next
    
    def sortlist(self):
        current = self.head
        index = None
        if(self.head == None):
            return
        else:
            while(current != None):
                index = current.next
                while(index != None):
                    if(current.data > index.data):
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next

list1 = linkedlist()
list1.insert(7) #memasukan data ke dalam linked list
list1.insert(19) #memasukan data ke dalam linked list
list1.insert(2) #memasukan data ke dalam linked list
list1.insert(5) #memasukan data ke dalam linked list
list1.insert(0) #memasukan data ke dalam linked list
print("Program untuk mengurutkan data dengan Linked List")
print("Data sebelum diurutkan : ", end=" ")
list1.tampilkan_data()
print(" ")
print("Data sesudah diurutkan : ", end=" ")
list1.sortlist()
list1.tampilkan_data()