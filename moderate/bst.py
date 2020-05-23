"""
Implement binary search tree
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert(self, value):
        if self.value == value:
            return False
        elif value < self.value:
            if self.left_child is None:
                self.left_child = Node(value)
                return True
            self.left_child.insert(value)
        else:
            if self.right_child is None:
                self.right_child = Node(value)
                return True
            self.right_child.insert(value)

    def contains(self, value):
        if self.value == value:
            return True
        if value < self.value:
            if self.left_child is None:
                return False
            else:
                self.left_child.contains(value)
        else:
            if self.right_child is None:
                return False
            else:
                self.right_child.contains(value)

    def inorder(self):
        if self is not None:
            if self.left_child is not None:
                self.left_child.inorder()
            print(self.value)
            if self.right_child is not None:
                self.right_child.inorder()

    def preorder(self):
        if self is not None:
            print(self.value)
            if self.left_child is not None:
                self.left_child.inorder()
            if self.right_child is not None:
                self.right_child.inorder()

    def postorder(self):
        if self is not None:
            if self.left_child is not None:
                self.left_child.inorder()
            if self.right_child is not None:
                self.right_child.inorder()
            print(self.value)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return True
        return self.root.insert(value)

    def contains(self, value):
        if self.root is None:
            return False
        return self.root.find(value)

    def remove(self, value):
        pass

    def traverse(self, travers_type="inorder"):
        if self.root is None:
            print("Tree is empty")
            return
        if travers_type == "inorder":
            self.root.inorder()
        elif travers_type == "preorder":
            self.root.preorder()
        elif travers_type == "postorder":
            self.root.postorder()
