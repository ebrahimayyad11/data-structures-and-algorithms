import sys
sys.path.append("/home/ebrahimayyad11/data-structures-and-algorithms/Data-Structures/k-ary-tree")
from k_ary_tree.k_ary_tree import Binary_Tree,Node


def fizz_buzz_tree(tr):
    if not tr.root:
        return "The Tree is Empty"
    else:
        node = tr.root
        queue = []
        queue += [node]
        while queue:
            node = queue[0]
            queue = queue[0:0] + queue[0 + 1:]

            if node.value%5 == 0 and node.value%3 == 0:
                node.value = 'FizzBuzz'
            elif node.value%5 == 0:
                node.value = 'Buzz'
            elif node.value%3 == 0:
                node.value = 'Fizz'
            else:
                node.value = str(node.value)

            if(node.left):
                queue += [node.left]
            if(node.right):
                queue += [node.right]

        return tr