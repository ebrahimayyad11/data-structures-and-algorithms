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
        Adds a new node to the head of the link list
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

    def append(self, value):
        """
        Adds a new node to the end of the link list
        """
        node = Node(value)
        if not self.head:
            self.head = node
            self.node_lst.append(self.head.value)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
            self.node_lst.append(current.next.value)

    def include(self, value):
        """
        Return True or False if value is in the linked list or not
        """
        if value in self.node_lst:
            return True
        else:
            return False

    def insertBefore(self, value, newValue):
        node = Node(newValue)
        for i in self.node_lst:
            if i == value:
                index_value = self.node_lst.index(i)
        self.node_lst.insert(index_value, node.value)
        return self.__str__()

    def insertAfter(self, value, newValue):
        node = Node(newValue)
        for i in self.node_lst:
            if i == value:
                index_value = self.node_lst.index(i)
        self.node_lst.insert(index_value+1, node.value)
        return self.__str__()

    def __str__(self):
        # "{ a } -> { b } -> { c } -> NULL"
        strr = ''
        for x in range(len(self.node_lst)):
            if x == 0:
                strr += ' { ' + str((self.node_lst[x])) + ' } -> '
            elif x == len(self.node_lst)-1:
                strr += '{ '+str((self.node_lst[x])) + ' }  -> NULL '
            else:
                strr += '{ '+str((self.node_lst[x])) + ' } -> '

        return strr

    def __repr__(self):
        return 'Nothing'


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(True)
    ll.append('ebrahim')
    ll.append(0)
    ll.insert(74)
    print(ll.insertBefore(True, 'hello world'))