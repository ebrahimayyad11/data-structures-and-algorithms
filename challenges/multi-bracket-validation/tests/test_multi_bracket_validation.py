from multi_bracket_validation import __version__
from multi_bracket_validation.multi_bracket_validation import multi_bracket_validation


def test_version():
    assert __version__ == '0.1.0'


def test_1():
    actual = multi_bracket_validation('{}')
    excepted = True
    assert actual == excepted

def test_2():
    actual = multi_bracket_validation('{}(){}')
    excepted = True
    assert actual == excepted


def test_3():
    actual = multi_bracket_validation('()[[Extra Characters]]')
    excepted = True
    assert actual == excepted



def test_4():
    actual = multi_bracket_validation('(){}[[]]')
    excepted = True
    assert actual == excepted



def test_5():
    actual = multi_bracket_validation('{}{Code}[Fellows](())')
    excepted = True
    assert actual == excepted

    
def test_6():
    actual = multi_bracket_validation('[({}]')
    excepted = False
    assert actual == excepted


def test_7():
    actual = multi_bracket_validation('(](')
    excepted = False
    assert actual == excepted


def test_8():
    actual = multi_bracket_validation('{(})')
    excepted = False
    assert actual == excepted


def test_9():
    actual = multi_bracket_validation('{')
    excepted = False
    assert actual == excepted


def test_10():
    actual = multi_bracket_validation(')')
    excepted = False
    assert actual == excepted


def test_11():
    actual = multi_bracket_validation('[}')
    excepted = False
    assert actual == excepted