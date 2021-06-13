from ll_insertions.ll_insertions import LinkedList
from ll_insertions import __version__


def test_version():
    assert __version__ == '0.1.0'


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
    assert ll.__str__() == " { 74 } -> { True } -> { a } -> { 0 }  -> NULL "


def test_include():  # 9
    ll = LinkedList()
    ll.append(True)
    ll.append('a')
    ll.append(0)
    ll.insert(74)
    assert ll.include('test') == False


def test_include_2():  # 10
    ll = LinkedList()
    ll.append(True)
    ll.append('ebrahim')
    ll.append(0)
    ll.insert(74)
    assert ll.include('ebrahim') == True


def test_insertBefore():  # 11
    ll = LinkedList()
    ll.append(True)
    ll.append('ebrahim')
    ll.append('test')
    ll.append(0)
    ll.insert(74)
    assert ll.insertBefore(
        True, 'hello world') == " { 74 } -> { hello world } -> { True } -> { ebrahim } -> { test } -> { 0 }  -> NULL "


def test_insertBefore_mid():  # 11
    ll = LinkedList()
    ll.append(True)
    ll.append('ebrahim')
    ll.append(0)
    ll.insert(74)
    assert ll.insertBefore(
        True, 'hello world') == " { 74 } -> { hello world } -> { True } -> { ebrahim } -> { 0 }  -> NULL "


def test_insertAfter():  # 12
    ll = LinkedList()
    ll.append(True)
    ll.append('ebrahim')
    ll.append(0)
    ll.insert(74)
    assert ll.insertAfter(
        True, 'hello world') == " { 74 } -> { True } -> { hello world } -> { ebrahim } -> { 0 }  -> NULL "