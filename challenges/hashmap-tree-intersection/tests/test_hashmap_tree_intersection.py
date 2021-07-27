import sys
sys.path.append("/home/ebrahimayyad11/data-structures-and-algorithms/Data-Structures/k-ary-tree")
from k_ary_tree.k_ary_tree import Binary_Tree,Node

from hashmap_tree_intersection import __version__
from hashmap_tree_intersection.hashmap_tree_intersection import tree_intersection



def test_version():
    assert __version__ == '0.1.0'


def test1():
    tr1 = Binary_Tree()
    tr2 = Binary_Tree()

    tr1.root = Node(2)
    tr1.root.left = Node(7)
    tr1.root.right = Node(5)
    tr1.root.left.left = Node(2)
    tr1.root.left.right = Node(6)
    tr1.root.right.right = Node(9)
    tr1.root.left.right.left = Node(5)
    tr1.root.left.right.right = Node(11)
    tr1.root.right.right.left = Node(4)


    tr2.root = Node(2)
    tr2.root.left = Node(7)
    tr2.root.right = Node(5)
    tr2.root.left.left = Node(2)
    tr2.root.left.right = Node(6)
    tr2.root.right.right = Node(9)
    tr2.root.left.right.left = Node(5)
    tr2.root.left.right.right = Node(11)
    tr2.root.right.right.left = Node(4)

    actual = tree_intersection(tr1,tr2)
    excepted = [2,7,2,6,5,11,5,9,4]
    assert actual == excepted


def test_tree_with_one_node():
    tr1 = Binary_Tree()
    tr2 = Binary_Tree()

    tr1.root = Node(2)
    tr1.root.left = Node(7)
    tr1.root.right = Node(5)
    tr1.root.left.left = Node(2)
    tr1.root.left.right = Node(6)
    tr1.root.right.right = Node(9)
    tr1.root.left.right.left = Node(5)
    tr1.root.left.right.right = Node(11)
    tr1.root.right.right.left = Node(4)


    tr2.root = Node(2)

    actual = tree_intersection(tr1,tr2)
    excepted = [2]
    assert actual == excepted

def test_empty_tree():
    tr1 = Binary_Tree()
    tr2 = Binary_Tree()

    tr1.root = Node(2)
    tr1.root.left = Node(7)
    tr1.root.right = Node(5)
    tr1.root.left.left = Node(2)
    tr1.root.left.right = Node(6)
    tr1.root.right.right = Node(9)
    tr1.root.left.right.left = Node(5)
    tr1.root.left.right.right = Node(11)
    tr1.root.right.right.left = Node(4)

    actual = tree_intersection(tr1,tr2)
    excepted = 'There is no match between the trees'
    assert actual == excepted


def test_no_match():
    tr1 = Binary_Tree()
    tr2 = Binary_Tree()

    tr1.root = Node(2)
    tr1.root.left = Node(7)
    tr1.root.right = Node(5)

    
    tr2.root = Node(4)
    tr2.root.left = Node(8)
    tr2.root.right = Node(6)

    actual = tree_intersection(tr1,tr2)
    excepted = 'There is no match between the trees'
    assert actual == excepted


