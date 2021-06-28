from sys import exec_prefix
from tree_breadth_first import __version__
from tree_breadth_first.tree_breadth_first import tree_breadth,Binary_Tree,Node


def test_version():
    assert __version__ == '0.1.0'

def test_1():
    tree = Binary_Tree()
    tree.root = Node(5)
    tree.root.left = Node(6)
    tree.root.left.right = Node(7)
    tree.root.right = Node(9)
    tree.root.right.left = Node(5)
    tree.root.left.right.right = Node(18)
    actual = tree_breadth(tree)
    expected = [5, 6, 9, 7, 5, 18]
    assert actual == expected



def test_2():
    tree = Binary_Tree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.right.right = Node(9)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right.right.left = Node(4)
    actual = tree_breadth(tree)
    expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
    assert actual == expected
