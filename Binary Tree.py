class book:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")

root=book("Harry Potter")
root.left=book("Dune")
root.right=book("The Lord of the Rings")
root.left.left=book("The Hobbit")
root.left.right=book("Ponniyin Selvan")

while True:
    print("\n\n1. Preorder")
    print("2. Inorder")
    print("3. Postorder")
    print("4. Exiting the program")

    ch=input("Enter your choice!")
   
    if ch=='1':
        preorder(root)
   
    elif ch=='2':
        inorder(root)

    elif ch=='3':
        postorder(root)

    elif ch=='4':    
        print("Exiting the program")
        break

    else:
        print("Invalid Input")
