import sys

class Node:
    def __init__(self, x, nextNode = None):
        self.val = x
        self.next = nextNode
 
def cetakList(l): # untuk cetak list yang masuk
    value = []
    while(l): # looping untuk mencetak index list yang ada
        value.append(l.val)
        l = l.next
    print(' '.join(map(str, value))) # cetak dengan spasi sebagai pemisah
 
def penjumlahan(l1, l2): # method penjumlahan list
    sum = l1.val + l2.val
    carry = int(sum / 10)
 
    l3 = Node(sum%10)
    p1 = l1.next
    p2 = l2.next
    p3 = l3
    while(p1 != None or p2 != None):
        sum = carry + ( p1.val if p1 else 0) + ( p2.val if p2 else 0)
        carry = int(sum/10)
        p3.next = Node(sum % 10)
        p3 = p3.next
        p1 = p1.next if p1 else None
        p2 = p2.next if p2 else None
 
    if(carry > 0):
        p3.next = Node(carry)
 
    return l3

#eksekusi program penjumlahan
print('Program Penjumlahan Dua Angka dari Linked List')
l1 = Node(6, Node(1, Node(9))) # jadinya didalam list pertama ada angka 6, 1, dan 9
sys.stdout.write('Nilai pada List ke-1 adalah              : ') 
cetakList(l1) #cetak list yang dimasukan
l2 = Node(7, Node(1, Node(1))) # jadinya didalam list pertama ada angka 7, 1, dan 1
sys.stdout.write('Nilai pada List ke-2 adalah              : ')
cetakList(l2) #cetak list yang dimasukan
l3 = penjumlahan(l1, l2)
sys.stdout.write('Hasil dari penjumlahan kedua list adalah : ')
cetakList(l3) #cetak list hasil penjumlahan list pertama dan kedua