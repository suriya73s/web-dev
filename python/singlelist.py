class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class linkedlist():
    def __init__ (self):
        self.head = None
    
    def addbegin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next  = self.head
            self.head = new_node
    def printll(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next
    def addend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.addbegin(data)
        else:
            n=self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
    def replace(self,index,data):
        position = 0
        n=self.head
        if position == index:
            n.data = data
        else:
            while(n is  not None and position != index):
                position = position+1
                n = n.next
            if n is not None:
                n.data = data
            else:
                print("index not found")            
    def nextchose(self,index,data):
        new_node = Node(data)
        n = self.head
        position = 0
        if index == 0:
            if n is None:
                n = new_node
            else:
                new_node.next = n
                n = new_node
        else:
            while(n is not None and position < index-1):
                position = position+1
                n = n.next
            if n is None:
                print("index erorr")
            else:
                new_node.next = n.next
                n.next = new_node                
    def delbegin(self):
        if self.head is None:
            print("list is empty")
        else:
            self.head = self.head.next
    def delend(self):
        if self.head is None:
            print("list is empty")
        elif self.head.next is None:
            self.head = None
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None
    def delselected(self,index):
        position = 0
        if self.head is None:
            print("list is empty")
        if position == index:
            self.delbegin()
        n = self.head
        while(n is not None and position+1 != index):
            position = position+1 
            n = n.next
        if self.head is None and n.next is None:
            print("not dound index")
        else:
            n.next = n.next.next
                
                      
            
ll = linkedlist()
ll.addbegin(23)
ll.addbegin(878)
ll.addbegin(1000)
ll.addbegin(10232300)
ll.addbegin(100120)
ll.nextchose(2,42000)
ll.delend()
ll.delselected(2)
ll.printll()

        