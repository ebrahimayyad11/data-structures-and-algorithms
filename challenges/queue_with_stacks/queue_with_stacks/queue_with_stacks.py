import sys
sys.path.append("//data-structures-and-algorithms/Data-Structures/stack-and-queue")
from stack_and_queue.stack_and_queue import Stack


class PseudoQueue:
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()
        self.count = 0

    def enqueue(self,value):
        self.stack_in.push(value)
        result = self.__str__  + '\n' + f'[{value}]' 
        return result


    def dequeue(self):
        if not self.stack_out.is_empty():
            while self.stack_out.top:
                self.stack_out.pop()

        while self.stack_in.top:
            self.stack_out.push(self.in_stack.pop())
            
        return self.stack_out.pop()

    def __str__(self):
        result = f'[{self.stack_in.top.value}]'
        current =self.stack_in.top.next
        while current:
            result += f' -> [{current.value}]'
            current = current.next
        return result