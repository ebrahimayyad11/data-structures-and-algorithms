from merge_sort import __version__
from merge_sort.merge_sort import Mergesort


def test_version():
    assert __version__ == '0.1.0'


def test_1():
    arr = [9,8,5,2,20,18,16]
    actual = Mergesort(arr)
    excepted = [2,5,8,9,16,18,20]
    assert actual == excepted


def test_2():
    arr = [9,8,5,2,20,18,16,35,80,1,3]
    actual = Mergesort(arr)
    excepted = [1,2,3,5,8,9,16,18,20,35,80]
    assert actual == excepted



def test_3():
    arr = [5,1,3,20,78,50]
    actual = Mergesort(arr)
    excepted = [1,3,5,20,50,78]
    assert actual == excepted