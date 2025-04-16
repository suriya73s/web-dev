class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_dfs(root):
    if root is None:
        return []
    return [root.val] + preorder_dfs(root.left) + preorder_dfs(root.right)

def inorder_dfs(root):
    if root is None:
        return []
    return inorder_dfs(root.left) + [root.val] + inorder_dfs(root.right)

def postorder_dfs(root):
    if root is None:
        return []
    return postorder_dfs(root.left) + postorder_dfs(root.right) + [root.val]

# Example usage
if __name__ == "__main__":
    # Creating the binary tree:
    #         1
    #       /   \
    #      2     3
    #     / \   / \
    #    4  5  6  7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print("Preorder DFS:  ", preorder_dfs(root))   # Expected: [1, 2, 4, 5, 3, 6, 7]
    print("Inorder DFS:   ", inorder_dfs(root))    # Expected: [4, 2, 5, 1, 6, 3, 7]
    print("Postorder DFS: ", postorder_dfs(root))  # Expected: [4, 5, 2, 6, 7, 3, 1]
