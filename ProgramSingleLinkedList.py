class Node(object):
    def __init__(self):
        self.data = None # yang nantinya akan diisikan data
        self.next = None # alamat untuk ke node selanjutnya
        
class LinkedList:
    def __init__(self):
        self.cur_node = None
        
    def add_node(self, data):
        new_node = Node()
        new_node.data = data
        new_node.next = self.cur_node
        self.cur_node = new_node
    
    def cetak(self):
        node = self.cur_node
        while node:
            print(node.data, end=' ')
            node = node.next
            
# eksekusi program
ll = LinkedList()
ll.add_node(7) # data pertama yang dimasukan
ll.add_node(3) # data kedua yang dimasukan
ll.add_node(1) # data ketiga yang dimasukan
ll.add_node(17) # data keempat yang dimasukan

print("Data yang dimasukan kedalam Linked List : ")
ll.cetak()