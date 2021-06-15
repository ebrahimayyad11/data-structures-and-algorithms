from ll_kth_from_end import __version__
from ll_kth_from_end.ll_kth_from_end import kth



def test_version():
    assert __version__ == '0.1.0'


def test1():
    actual = kth(0)
    expected = 2
    assert actual == expected

def test2():
    actual = kth(2)
    expected = 3
    assert actual == expected


def test1():
    actual = kth(6)
    expected = Exception
    assert actual == expected