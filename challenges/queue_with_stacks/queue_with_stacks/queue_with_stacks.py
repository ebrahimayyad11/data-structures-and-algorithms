import sys
sys.path.append("/home/ebrahimayyad11/data-structures-and-algorithms/Data-Structures/stack-and-queue")
from stack_and_queue.stack_and_queue import Stack


class PseudoQueue:
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def enqueue(self,value):
        self.stack_in.push(value)


    def dequeue(self):
        if  self.stack_in.top == None:
            return 'there is no data'
        else: 
            current1 = self.stack_in.top
            while current1:
                self.stack_out.push(self.stack_in.pop())
                current1 = self.stack_in.top
            result = self.stack_out.pop()
            current2 = self.stack_out.top
            while current2:
                self.stack_in.push(self.stack_out.pop())
                current2 = self.stack_out.top
            return f'[{result}]'

    