class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.inorder_predecor(root.left)
            root.key = temp.key
            root.left1 = self.delete(root.left, temp.key)
        return root
    
#finding inorder successor --> smallest node in right subtree 
    def find_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current
    
    #had to add this
    def inorder_predecor(self, root):
        current = root
        while current.right is not None:
            current = current.right 
        return current 

    



    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")


def menu():
    bst = BinarySearchTree()
    while True:
        print("\n--- Binary Search Tree Menu ---")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Inorder Traversal")
        print("5. Preorder Traversal")
        print("6. Postorder Traversal")
        print("7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter key to insert: "))
            bst.root = bst.insert(bst.root, key)
        elif choice == 2:
            key = int(input("Enter key to delete: "))
            bst.root = bst.delete(bst.root, key)
        elif choice == 3:
            key = int(input("Enter key to search: "))
            result = bst.search(bst.root, key)
            if result:
                print(f"Key {key} found in the tree.")
            else:
                print(f"Key {key} not found in the tree.")
        elif choice == 4:
            print("Inorder Traversal: ", end="")
            bst.inorder(bst.root)
            print()
        elif choice == 5:
            print("Preorder Traversal: ", end="")
            bst.preorder(bst.root)
            print()
        elif choice == 6:
            print("Postorder Traversal: ", end="")
            bst.postorder(bst.root)
            print()
        elif choice == 7:
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    menu()


