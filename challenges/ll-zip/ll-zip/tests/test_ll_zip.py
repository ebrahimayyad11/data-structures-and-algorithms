from ll_zip.linked_list import LinkedList
from ll_zip import __version__
from ll_zip.ll_zip import ll_zip


def test_version():
    assert __version__ == '0.1.0'


def test_ll_zip_1():
    ll1 = LinkedList()
    ll2 = LinkedList()

    ll1.append(1)
    ll1.append(3)
    ll1.append(2)

    ll2.append(5)
    ll2.append(9)
    ll2.append(4)

    excepted = 'Head -> (1) -> (5) -> (3) -> (9) -> (2) -> (4) -> Null'
    actual = ll_zip(ll1,ll2)
    assert actual == excepted


def test_ll_zip_2():
    ll1 = LinkedList()
    ll2 = LinkedList()

    ll1.append(1)
    ll1.append(3)

    ll2.append(5)
    ll2.append(9)
    ll2.append(4)

    excepted = 'Head -> (1) -> (5) -> (3) -> (9) -> (4) -> Null'
    actual = ll_zip(ll1,ll2)
    assert actual == excepted


def test_ll_zip():
    ll1 = LinkedList()
    ll2 = LinkedList()

    ll1.append(1)
    ll1.append(3)
    ll1.append(2)

    ll2.append(5)
    ll2.append(9)

    excepted = 'Head -> (1) -> (5) -> (3) -> (9) -> (2) -> Null'
    actual = ll_zip(ll1,ll2)
    assert actual == excepted