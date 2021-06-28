import sys
sys.path.append("/home/ebrahimayyad11/data-structures-and-algorithms/Data-Structures/k-ary-tree")
from k_ary_tree.k_ary_tree import Binary_Tree,Node


def tree_breadth(tr):
    if not tr.root:
        return "The Tree is Empty"
    else:
        node = tr.root
        data = []
        queue = []
        queue += [node]
        while queue:
            node = queue[0]
            queue = queue[0:0] + queue[0 + 1:]

            data += [node.value]

            if(node.left):
                queue += [node.left]
            if(node.right):
                queue += [node.right]

        return data
        