class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None
    
class linkedlist():
    def __init__ (self):
        self.head=None
    
    def addbegin(self,data):
        new_node = Node(data)
        new_node.next  = self.head
        self.head = new_node

    
    def addend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n= self.head
            while n.next is not None:
                n= n.next
            n.next = new_node
                
    def printll(self):
        if self.head is None:
            print("list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.next  
           
  

ll = linkedlist()
ll.addend(45232345)
ll.printll()