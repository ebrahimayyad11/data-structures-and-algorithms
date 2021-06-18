import linked_list


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


"""
Draft:
ll: head - None
ll.append(4)
ll: head - Node(4) -> None
ll.append(-1)
ll: head - Node(4) -> Node(-1) -> None
ll.append('s')
ll: head - Node(4) -> Node(-1) -> Node('s') -> None
"""


class LinkedList:
    def __init__(self):
        self.node_lst = []
        self.head = None

    def insert(self, value):
        """
        Adds a node of a value to the head of LL
        """
        node = Node(value)
        if self.head is None:
            self.head = node
            self.node_lst.insert(0, self.head.value)
        else:
            current = self.head
            self.head = node
            node.next = current
            self.node_lst.insert(0, self.head.value)

    def append(self,value):
        """
        Adds a node of a value to the end of LL
        """

        current=self.head
        if self.head ==None:
            self.head=Node(value)
            return self.head.value
        else:
            while current.next:
                current=current.next
            current.next=Node(value)
            return current.next
      
       
    def include(self, value):
        """
        Return True or False if value is in the linked list or not
        """
        if value in self.node_lst:
            return True
        else:
            return False

    
        
    def __str__(self):
        # "{ a } -> { b } -> { c } -> NULL"
        if self.head == None:
            return 'NULL'
        else :
            values=''
            temporary_value=self.head
            while temporary_value:
                values+='{'+ f'{temporary_value.value}' +'} ' + '-> ' 
                temporary_value=temporary_value.next
            values=values +'NULL'
            return f'{values}'
    def __repr__(self):
        return 'Nothing'
    

    def insert_before(self,val,new_val):
        try:
            current=self.head
            if self.head ==None:
                self.head=Node(val)
                return self.head
            elif current.value == val:
                       self.insert(new_val)
            else:
                while current: 
                    if  current.next.value== val:
                        saved_current_val=current.next
                        current.next=Node(new_val)
                        current.next.next=saved_current_val 
                        return current.next
                    current=current.next
        except:
            raise Exception ('Error')


    
    def insert_after(self,val,new_val):
            try:
                current=self.head
                if self.head ==None:
                  self.head=Node(val)
                  return self.head
                else:
                  while current: 
                    if  current.value== val:
                        saved_current_val=current.next
                        current.next=Node(new_val)
                        current.next.next=saved_current_val 
                        return current.next
                    current=current.next
            except:
                raise Exception ('Error')

    
    def kthFromEnd(self,k):
        if k < 0 or k >= len(self.node_lst):
            return 'Unavailable Index'
        else:
            arr=[]
            index = 0
            for i in self.node_lst:
                arr += str(0)
                arr[index] = i
                index += 1
            return arr[k]



            
            




