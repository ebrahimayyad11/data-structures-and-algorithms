from linked_list.linked_list import LinkedList
from linked_list import __version__


def test_version():  # 1
    assert __version__ == '0.1.0'


def test_append_1():  # 2
    ll = LinkedList()
    ll.append(1)
    assert ll.head.value == 1


def test_append_2():  # 3
    ll = LinkedList()
    ll.append(1)
    ll.append(5)
    ll.append(73)
    assert ll.head.next.value == 5


def test_append_3():  # 4
    ll = LinkedList()
    ll.append(1)
    ll.append(5)
    ll.append(73)
    assert ll.head.next.next.value == 73


def test_insert_1():  # 5
    ll = LinkedList()
    ll.insert(6)
    assert ll.head.value == 6


def test_insert_2():  # 6
    ll = LinkedList()
    ll.append(0)
    ll.append('a')
    ll.append(True)
    ll.insert(12)
    assert ll.head.value == 12


def test_insert_3():  # 7
    ll = LinkedList()
    ll.append(0)
    ll.append('a')
    ll.append(True)
    ll.insert(12)
    assert ll.head.next.next.value == 'a'


def test_str():  # 8
    ll = LinkedList()
    ll.append(True)
    ll.append('a')
    ll.append(0)
    ll.insert(74)
    ll.__str__()
    assert ll.__str__() == "{74} -> {True} -> {a} -> {0} -> NULL"


def test_include():  # 9
    ll = LinkedList()
    ll.append(True)
    ll.append('a')
    ll.append(0)
    ll.insert(74)
    assert ll.include('test') == False





def test_add_node_to_end_of_linked_list():
    lnk_lst=LinkedList()
    excepted= 8
    actual = lnk_lst.append(8)
    # actual = lnk_lst
    assert excepted==actual

def test_add_multiple_nodes_to_end_of_linked_list():
    lnk_lst=LinkedList()
    lnk_lst.append(8)
    lnk_lst.append(3)
    lnk_lst.append('b')
    excepted='{8} -> {3} -> {b} -> NULL'
    actual=lnk_lst.__str__()
    assert excepted==actual

def test_insert_node_before_node_middle_of_linked_list():
    lnk_lst=LinkedList()
    lnk_lst.append(8)
    lnk_lst.append(3)
    lnk_lst.append('b')
    lnk_lst.append('4')
    lnk_lst.insert_before('b',7)
    excepted='{8} -> {3} -> {7} -> {b} -> {4} -> NULL'
    actual=lnk_lst.__str__()
    assert excepted==actual


def test_insert_node_before_the_first_node():
    lnk_lst=LinkedList()
    lnk_lst.append(8)
    lnk_lst.append(3)
    lnk_lst.insert_before(8,'a')
    excepted='{a} -> {8} -> {3} -> NULL'
    actual=lnk_lst.__str__()
    assert excepted==actual

def test_insert_after_node_middle_of_linked_list():
    lnk_lst=LinkedList()
    lnk_lst.append(8)
    lnk_lst.append(3)
    lnk_lst.append('b')
    lnk_lst.append('4')
    lnk_lst.insert_after('b',7)
    excepted='{8} -> {3} -> {b} -> {7} -> {4} -> NULL'
    actual=lnk_lst.__str__()
    assert excepted==actual

def test_insert_node_after_last_node():
    lnk_lst=LinkedList()
    lnk_lst.append(8)
    lnk_lst.append(3)
    lnk_lst.insert_after(8,'a')
    excepted='{8} -> {a} -> {3} -> NULL'
    actual=lnk_lst.__str__()
    assert excepted==actual
