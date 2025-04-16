class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.recinsert(value, self.root)

    def recinsert(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.recinsert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self.recinsert(value, node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" -> ")
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" -> ")

    def search(self, value):
        return self.recsearch(value, self.root)

    def recsearch(self, value, node):
        if node is None or value == node.value:
            return node
        elif value < node.value:
            return self.recsearch(value, node.left)
        else:
            return self.recsearch(value, node.right)

    def delete(self, value):
        self.root = self._delete(value, self.root)

    def _delete(self, value, node):
        if not node:
            return None
        if value < node.value:
            node.left = self._delete(value, node.left)
        elif value > node.value:
            node.right = self._delete(value, node.right)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._find_min(node.right)
            node.value = temp.value
            node.right = self._delete(temp.value, node.right)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node


# Driver Code
bst = tree()
bst.insert(10)
bst.insert(210)
bst.insert(100)

print("Inorder before delete:")
bst.inorder(bst.root)

bst.delete(10)

print("\nInorder after deleting 10:")
bst.inorder(bst.root)

print("\nSearch 20:", "20 found" if bst.search(20) else "Not found")
