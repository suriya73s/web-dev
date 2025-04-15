class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right =None

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
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.value,end="->")
            self.inorder(node.right)
     
    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ->")
               
    def search(self,value):
        
       return self.recsearch(value,self.root)
        
    def recsearch(self,value,node):
        if node is None or value == node.value:
            return node
        elif value < node.value:
            return self.recsearch(value,node.left)
        else:
            return self.recsearch(value,node.right)
        
    def delete(self,value):
        self.recdelete(value,self.root)
    
    def recdelete(self,value,node):
        if node is None:
            return None
        if value < node.value:
            node.left = self.recdelete(value,node.left)
        else:
            node.right = self.recdelete(value,node.right)
        if node.left is None:
            return node.left
        if node.right is None:
            return node.right
            
bst = tree()
bst.insert(10)
bst.insert(210)
bst.insert(100)
bst.inorder(bst.root)
print("\nsearch 20", " 20 found" if bst.search(20) else "not found")

        
        