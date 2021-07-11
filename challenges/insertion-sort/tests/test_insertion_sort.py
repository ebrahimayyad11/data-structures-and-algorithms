from insertion_sort import __version__
import insertion_sort
from insertion_sort.insertion_sort import InsertionSort


def test_version():
    assert __version__ == '0.1.0'


def test_1():
    arr = [9,8,5,2,20,18,16]
    actual = InsertionSort(arr)
    excepted = [2,5,8,9,16,18,20]
    assert actual == excepted


def test_2():
    arr = [9,8,5,2,20,18,16,35,80,1,3]
    actual = InsertionSort(arr)
    excepted = [1,2,3,5,8,9,16,18,20,35,80]
    assert actual == excepted



def test_3():
    arr = [5,1,3,20,78,50]
    actual = InsertionSort(arr)
    excepted = [1,3,5,20,50,78]
    assert actual == excepted