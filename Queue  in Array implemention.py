class parking:
    def __init__(self):
        self.max=10
        self.front=-1
        self.rear=-1
        self.parking=[]
    def enqueue_car(self,data):
        if self.max>=self.rear:
            self.parking.append(data)
            self.rear+=1
            self.front=0
        elif self.max>=self.rear:                                            
            self.parking.append(data)
            self.rear+=1
        else:
            print("parking is full")
    def dequeue_car(self):
        if self.rear==0:
            print("parking is empty")
            return
        else:
            print(f"{self.parking[self.front]} is removed")
            self.front+=1
        if self.rear==self.front:
            self.rear=self.front=-1
    def display_all(self):
        st=self.front
        ed=self.rear
        for i in range(st,ed+1):
            print(f"{self.parking[i]}-->",end="")
        print(None)
obj=parking()

while True:
    ch=int(input("enter choice:"))
    if ch==1:
        n=int(input("Enter no of elements:"))
        for i in range(n):
            a=int(input(f"Enter element{i+1}:"))
            obj.enqueue_car(a)
    elif ch==2:
        obj.dequeue_car()
    elif ch==3:
        obj.display_all()
    else:
        break
