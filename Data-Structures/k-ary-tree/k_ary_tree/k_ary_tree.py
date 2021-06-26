class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Binary_Tree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        try:    
            """
            a function that return the tree in (pre order) 
            """
            if not self.root:
                  return "the tree is empty!"
            else:
              result = []
              def tree(node):
                nonlocal result
                result += [node.value]
                if node.left:
                  tree(node.left)
                if node.right:
                  tree(node.right)
                return result
              return tree(self.root)
        except:
            print("something went wrong please try again")

    def in_order(self):
        """
            a function that return the tree in (in order) 
        """
        try:        
            if not self.root:
                  return "the tree is empty!"
            else:
              result = []
              def tree(node):
                if node.left:
                  tree(node.left)
                nonlocal result
                result += [node.value]
                if node.right:
                  tree(node.right)
                return result
              return tree(self.root) 
        except:
            print("something went wrong please try again")

    def post_order(self):
        """
            a function that return the tree in (post order) 
        """
        try:
          if not self.root:
                  return "the tree is empty!"
          else:
            result = []
            def tree(node):
                if node.left:
                  tree(node.left)
                if node.right:
                  tree(node.right)
                nonlocal result
                result += [node.value]
                return result
            final_result = tree(self.root)
            return final_result 
        except:
            print("something went wrong please try again")



class Binary_Search_Tree(Binary_Tree):
    def __init__(self):
        super().__init__()
    
    def add(self, value):
        """
        to add a new value to the tree 
        """
        try:
            if not self.root:
                self.root = Node(value)
            else:
                node = self.root
                while node:
                    if node.value > value: 
                        if not node.left:
                            node.left = Node(value)
                            break
                        node = node.left
                    else:
                        if not node.right: 
                            node.right = Node(value)
                            break
                        node = node.right
        except:
            print("something went wrong please try again")       
    
    
    def contains(self, value):
        """
        function return true if the tree contain the value or value not found 
        """
        try:
            if not self.root:
                return 'The Tree is empty'
            else:
                node = self.root
                while node:
                    if node.value==value:
                        return True
                    if node.value > value: 
                        if not node.left: 
                            return 'The value is not in the Tree'
                        node = node.left
                    else:
                        if node.right == None: 
                            return 'The value is nor in the Tree'
                        node = node.right
        except:
            print("something went wrong please try again")       
                



if __name__ == '__main__':
    tree = Binary_Search_Tree()
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(4)
    tree.add(3)
    print(tree.pre_order())
    print(tree.in_order())
    print(tree.post_order())