import sys
sys.path.append("/home/ebrahimayyad11/data-structures-and-algorithms/Data-Structures/stack-and-queue")
from stack_and_queue.stack_and_queue import Queue


class AnimalShelter :
    cat = Queue()
    dog = Queue()

    def __init__(self):
        pass


    def enqueue(self, name, type):
        if type =='dog' or type =='DOG':
            self.dog.enqueue(name)        
        elif type =='cat' or type =='CAT':
            self.cat.enqueue(name)        
        else:
            return 'you can just choose dog or cat'


    
    def dequeue(self, type = None):
        if type == 'dog' or type =='DOG':
            return self.dog.dequeue()
        elif type =='cat' or type =='CAT':
            return self.cat.dequeue()
        elif type == None:
            return 'enter the type of the animal'
        else:
            return 'you can just choose dog or cat'


    