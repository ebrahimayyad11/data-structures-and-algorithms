class Node():
    def __init__(self,value):
        self.value=value
        self.next=None



class Stack():
    def __init__(self):
        self.top=None

    def push(self,value):
        current=self.top
        self.top=Node(value)
        self.top.next=current
        return self.top.value

    def pop(self):
        try:
            if not self.top:
               raise Exception
            else:
              pop = self.top.value
              self.top=self.top.next
              return pop
        
        except Exception:
            return 'The Stack is empty!'    

    def peek(self):
        try:
            if not self.top:
               raise Exception

            return self.top.value

        except Exception:
            return 'The Stack is empty!'

    def isEmpty(self):
         return self.top ==None



class Queue():
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue (self,value):
        node=Node(value)
        if self.rear==None:
            self.front=node
            self.rear=node
            return self.rear.value
        else:
            self.rear.next=node
            self.rear=node
            return self.rear.value

    def dequeue(self):
        try:
            if not self.front:
                raise Exception
            else:
              temp=self.front
              self.front=self.front.next
              return temp.value

        except Exception:
            return 'The Queue is empty!'

    def peek (self):
        try:
            if not self.front:
                raise Exception
            else:
              return self.front.value

        except Exception:
            return 'The Queue is empty!'

    def isEmpty(self):
        return self.front==None

