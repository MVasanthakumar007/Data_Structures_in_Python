class Stack:
    def __init__(self):
        self.stack=[]
   
    def push(self,item):
        self.stack.append(item)
        print("Book added to the stack")

    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        return self.stack.pop()
   
    def peek(self):
        if self.is_empty():
            return "Stack is Empty."
        return self.stack[-1]
   
    def is_empty(self):
        return len(self.stack)==0

    def size(self):
        return len(self.stack)
   
    def display(self):
        print("Stack elements:",self.stack)


ob=Stack()

while True:
    print("1. Pushing an book into the stack")
    print("2. Popping an book into the stack")
    print("3. Peeking")
    print("4. Check whether the stack is empty")
    print("5. Displaying size of the book stack")
    print("6. Displaying all the books in the stack")
    print("7. Exiting the program")


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
        e=ob.size()
        print(e)
   
    elif ch=='6':
        f=ob.display()
        print(f)
   
    elif ch=='7':    
        print("Exiting the program")
        break

    else:
        print("Invalid Inputd")
