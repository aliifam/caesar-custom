class Node():
    def __init__(self, data): #constructor
        self.data = data
        self.next = None

class linkstack():
    def __init__(self): #constructor
        self.head = None
        self.tail = None
    
    def pushData(self, data): #truelly it's = addHead
        newdata = Node(data)
        if self.head == None:
            self.head = newdata
            self.tail = newdata
        else:
            newdata.next = self.head
            self.head = newdata
    
    def removeHead(self): #truelly it's = removeHead
        if self.head == None:
            print("error stack sudah kosong")
        elif self.head.next == None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
    
    def peekHead(self): #truelly it's = peekHead
        if self.head == None:
            return "error stack sudah kosong"
        else:
            return self.head.data

def main():

    list_angka = input().split(" ")
    list_angka = list(map(int, list_angka))
    panjang = len(list_angka)


    ll = linkstack()

    for i in list_angka:
        ll.pushData(i)

    for i in range(panjang):
        print(ll.peekData(), end=" ")
        ll.popData()

main()