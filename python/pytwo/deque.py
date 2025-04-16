class NOde:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class linked:
    def __init__(self):
        self.head = None
    
    def insertstart(self,data):
        newnode=NOde(data)
        if self.head is None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode
    def insertend(self, data):
        newnode = NOde(data)
        if self.head is None:
            self.head = newnode
        else:
            currentnode = self.head
            while currentnode.next:
                currentnode = currentnode.next
            currentnode.next = newnode
    def printll(self):
        cur = self.head
        while cur:
            print(cur.data,end=" - ")
            cur = cur.next    
    def delindex(self,index):    
        position = 0
        if position == index:
            self.head = self.head.next
            self.head = self.head
        curnode= self.head
        while curnode != None and position+1 != index:
            position = position+1
            curnode = curnode.next
        if curnode.next is None:
            print("element bnot dound")
        curnode.next = curnode.next.next
    def delend(self):
        if self.head is None:
            print("ser")  
        else:
            cd = self.head
            while cd.next.next is not None:
                cd =cd.next
            if cd.next is None:
                cd = cd.next
            cd.next = cd.next.next
                
               

li = linked()
li.insertstart(20)
li.insertend(50)
li.insertstart(23)
li.insertend(100)
li.delindex(1)
li.delend()
li.printll()
