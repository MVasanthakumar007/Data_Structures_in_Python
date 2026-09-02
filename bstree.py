class Node:
    def __init__(self, name, time):
        self.name = name
        self.time = time
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, name, time):
        new_node = Node(name, time)
        if self.root is None:
            self.root = new_node
            print("Entry inserted successfully.")
            return
        current = self.root
        while True:
            if name < current.name:
                if current.left is None:
                    current.left = new_node
                    print("Entry inserted successfully.")
                    return
                current = current.left
            elif name > current.name:
                if current.right is None:
                    current.right = new_node
                    print("Entry inserted successfully.")
                    return
                current = current.right
            else:
                print("Visitor name already exists.")
                return
    def search(self, name):
        current = self.root
        while current is not None:
            if name == current.name:
                print("Entry found!")
                print("Visitor Name:", current.name)
                print("Entry Time:", current.time)
                return
            elif name < current.name:
                current = current.left
            else:
                current = current.right
        print("Entry not found.")
    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    def delete(self, node, name):
        if node is None:
            return node
        if name < node.name:
            node.left = self.delete(node.left, name)
        elif name > node.name:
            node.right = self.delete(node.right, name)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self.find_min(node.right)
            node.name = temp.name
            node.time = temp.time
            node.right = self.delete(node.right, temp.name)
        return node
    def traverse(self, node, order):
        if node is None:
            return
        if order == "inorder":
            self.traverse(node.left, order)
            print(node.name, "-", node.time)
            self.traverse(node.right, order)
        elif order == "postorder":
            self.traverse(node.left, order)
            self.traverse(node.right, order)
            print(node.name, "-", node.time)
    def count(self, node):
        if node is None:
            return 0
        return 1 + self.count(node.left) + self.count(node.right)
bst = BinarySearchTree()
print("\n===== LOG BOOK MENU =====")
print("1. Insert Entry")
print("2. Delete Entry")
print("3. Search Entry")
print("4. Inorder Traversal")
print("5. Postorder Traversal")
print("6. Count Total Entries")
print("7. Exit")
while True:
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter visitor name: ")
        time = input("Enter entry time: ")
        bst.insert(name, time)
    elif choice == "2":
        name = input("Enter visitor name to delete: ")
        if bst.root is None:
            print("Log book is empty.")
        else:
            bst.root = bst.delete(bst.root, name)
            print("Delete operation completed.")
    elif choice == "3":
        name = input("Enter visitor name to search: ")
        bst.search(name)
    elif choice == "4":
        if bst.root is None:
            print("Log book is empty.")
        else:
            print("Inorder Traversal:")
            bst.traverse(bst.root, "inorder")
    elif choice == "5":
        if bst.root is None:
            print("Log book is empty.")
        else:
            print("Postorder Traversal:")
            bst.traverse(bst.root, "postorder")
    elif choice == "6":
        print("Total number of entries:", bst.count(bst.root))
    elif choice == "7":
        print("Exiting program...")
        break
    else:
        print("Invalid choice.")

