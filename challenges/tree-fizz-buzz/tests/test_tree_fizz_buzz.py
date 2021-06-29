from tree_fizz_buzz import __version__
from tree_fizz_buzz.tree_fizz_buzz import Binary_Tree,Node,fizz_buzz_tree


def test_version():
    assert __version__ == '0.1.0'


def test_fizz_buzz():
    tree = Binary_Tree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    actual = fizz_buzz_tree(tree).pre_order()
    excepted = ['2', '7', '2', 'Fizz', 'Buzz']
    assert actual == excepted

def test_empty_tree():
    tree = Binary_Tree()
    actual = fizz_buzz_tree(tree)
    excepted = 'The Tree is Empty'
    assert actual == excepted
