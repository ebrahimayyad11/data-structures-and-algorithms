from quick_sort import __version__
from quick_sort.quick_sort import QuickSort


def test_version():
    assert __version__ == '0.1.0'


def test_empty_list():
    array = []
    actual = QuickSort([])
    expected = []
    assert actual == expected

def test_one_item_list():
    array = [5]
    actual = QuickSort(array)
    expected = [5]
    assert actual == expected

def test_two_item_list():
    array = [5,2]
    actual = QuickSort(array)
    expected = [2,5]
    assert actual == expected

def test_many_item_list():
    array = [1,5,2,-4,88]
    actual = QuickSort(array)
    expected = [-4, 1, 2, 5, 88]
    assert actual == expected
