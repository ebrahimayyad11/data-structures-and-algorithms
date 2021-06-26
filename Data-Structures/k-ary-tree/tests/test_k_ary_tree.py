from k_ary_tree import __version__
from k_ary_tree.k_ary_tree import Binary_Tree,Binary_Search_Tree


def test_version():
    assert __version__ == '0.1.0'


def test_empty_tree():
    tree = Binary_Search_Tree()
    actual = tree.root
    expected = None
    assert actual == expected

def test_tree_single_node():
    tree = Binary_Search_Tree()
    tree.add(10)
    actual = tree.root.value
    expected = 10
    assert actual == expected

def test_add_left_right():
    tree = Binary_Search_Tree()
    tree.add(10)
    tree.add(9)
    tree.add(11)
    result = [tree.root.left.value,tree.root.right.value]
    actual = result
    expected = [9,11]
    assert actual == expected

def test_pre_order():
    tree = Binary_Search_Tree()
    tree.add(10)
    tree.add(9)
    tree.add(11)
    actual = tree.pre_order()
    excepted = [10,9,11]
    assert actual == excepted

def test_in_order():
    tree = Binary_Search_Tree()
    tree.add(10)
    tree.add(9)
    tree.add(11)
    actual = tree.in_order()
    excepted = [9,10,11]
    assert actual == excepted

def test_post_order():
    tree = Binary_Search_Tree()
    tree.add(10)
    tree.add(9)
    tree.add(11)
    actual = tree.post_order()
    excepted = [9,11,10]
    assert actual == excepted

