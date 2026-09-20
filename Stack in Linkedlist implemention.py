class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None

    def is_empty(self):
        return self.top is None
   
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.top
        self.top=new_node
        print(f"Book added to the stack")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        popped_data=self.top.data
        self.top=self.top.next
        return popped_data
   
    def peek(self):
        if self.is_empty():
            print("Stack is Empty.")
            return None
        return self.top.data
 
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        print("\n Current Stack:")
        current=self.top
        while current is not None:
            print(f"[{current.data}]->",end="")
            current=current.next
        print("NULL \n")


ob=Stack()

while True:
    print("1. Pushing an book into the stack")
    print("2. Popping an book into the stack")
    print("3. Peeking")
    print("4. Check whether the stack is empty")
    print("5. Displaying all the books in the stack")
    print("6. Exiting the program")


    ch=input("Enter your choice!")
   
    if ch=='1':
        a=input("Enter book name to push:")
        ob.push(a)
   
    elif ch=='2':
        b=ob.pop()
        print("Book removed from the stack")

    elif ch=='3':
        c=ob.peek()
        print(c)

    elif ch=='4':
        d=ob.is_empty()
        print(d)
   
    elif ch=='5':
        f=ob.display()
        print(f)
   
    elif ch=='6':    
        print("Exiting the program")
        break

    else:
        print("Invalid Input")
