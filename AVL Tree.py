class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


def height(root):
    if root is None:
        return 0
    return root.height


def balance(root):
    if root is None:
        return 0
    return height(root.left) - height(root.right)
def right_rotate(y):
    x = y.left
    t = x.right

    x.right = y
    y.left = t

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))
    return x
def left_rotate(x):
    y = x.right
    t = y.left
    y.left = x
    x.right = t
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)

    elif data > root.data:
        root.right = insert(root.right, data)

    else:
        return root

    root.height = 1 + max(height(root.left), height(root.right))
    b = balance(root)
    if b > 1 and data < root.left.data:
        return right_rotate(root)
    if b < -1 and data > root.right.data:
        return left_rotate(root)
    if b > 1 and data > root.left.data:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if b < -1 and data < root.right.data:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    return root
def search(root, data):
    if root is None:
        return False

    if root.data == data:
        return True

    if data < root.data:
        return search(root.left, data)

    return search(root.right, data)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
def count(root):
    if root is None:
        return 0
    return 1 + count(root.left) + count(root.right)
root = None
print("\n1. Insert")
print("2. Search")
print("3. Inorder Traversal")
print("4. Count")
print("5. Exit")
while True:

    choice = int(input("Enter choice: "))
    if choice == 1:
        value = int(input("Enter value: "))
        root = insert(root, value)
        print("Value inserted")

    elif choice == 2:
        value = int(input("Enter value to search: "))

        if search(root, value):
            print("Value found")
        else:
            print("Value not found")

    elif choice == 3:
        print("Inorder:", end=" ")
        inorder(root)
        print()

    elif choice == 4:
        print("Total nodes:", count(root))

    elif choice == 5:
        print("Program ended")
        break

    else:
        print("Invalid choice")
