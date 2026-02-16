# Binary tree is an example of using tree data structure

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# Added another class to handle the structure and behavior while the previous class handles the data
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = BinaryTree(data)
        else:
            self._insert_recursive(self.root, data)
# helper for insert   
    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = BinaryTree(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = BinaryTree(data)
            else:
                self._insert_recursive(node.right, data)

    def search(self,data):
        return self._search_recursive(self.root, data)

    # helper for search function
    def _search_recursive(self, node, data):
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)
    
    def search (self, data):
        return self._search_recursive(self.root, data)
    
    # Helper method for Search method
    def _search_recursive(self, node, data):
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)


bst = BinarySearchTree()

values = [50, 30, 70, 20, 40, 60, 80]
for v in values:
    bst.insert(v)

print("Inorder traversal (sorted):", bst.inorder_traversal())

    # Search tests
print("Search 40:", bst.search(40))
print("Search 100:", bst.search(100)
