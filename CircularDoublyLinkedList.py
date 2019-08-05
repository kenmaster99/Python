class _DoublyLinkedList:
    
    class _Node(object):
        __slots__ = '_element', '_prev','_next'
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
            
        def getNext(self):
            return self._next
        
        def __str__(self):
            return str(self._element)
        
    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

    def first(self): #return but do not remove the element at front
        if self.is_empty():
            raise Empty("Empty!")
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Empty("Empty!")
        return self._trailer._prev._element

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty("Empty!")
        return self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Empty("Empty!")
        return self._delete_node(self._trailer._prev)

    def __str__(self):
        if self._size == 0:
            return '[]'
        retString = "["
        currentElement = self._header.getNext()
        for i in range(self._size):
            retString += str(currentElement) +", "
            currentElement = currentElement.getNext()

        return retString[:-2] + ']'
        
adit = _DoublyLinkedList()
adit.insert_first(17)
print("Hasil dari input pertama dengan Insert First adalah :", end=' ')
print(adit.__str__())
adit.insert_last(1)
print("Hasil dari input Kedua dengan Insert Last adalah :", end=' ')
print(adit.__str__())
adit.insert_first(7)
print("Hasil dari input Ketiga dengan Insert First (lagi) adalah :", end=' ')
print(adit.__str__())
adit.delete_first()
print("Hasil dari Method delete first adalah :", end=' ')
print(adit.__str__())
adit.delete_last()
print("Hasil dari Method delete last adalah :", end=' ')
print(adit.__str__())