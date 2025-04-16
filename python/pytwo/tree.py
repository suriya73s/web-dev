class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
class tree:
    def __init__(self):
        self.root = None
    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.recinsert(value,self.root)
    def recinsert(self,value,node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.recinsert(value,node.left)
        if value > node.value:
            if node.right is None:
                node.right = Node(value)  
            else:
                self.recinsert(value,node.right)
    
    def search(self,value,node):
        if node is not None and value == node.value:
            return node
        elif value < node.value:
            return self.search(value,node.left)
        else:
            return self.search(value,node.right)
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.value,end = "->")
            self.inorder(node.right)
            
tr = tree()
tr.insert(10)
tr.insert(12)
tr.insert(1)
print("found" if tr.search(12,tr.root) else "not found")
tr.inorder(tr.root)