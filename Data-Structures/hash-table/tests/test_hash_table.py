from hash_table import __version__
from hash_table.hash_table import Hashtable


def test_version():
    assert __version__ == '0.1.0'

########## tests #########


def test_hash_add(): ## test 1
    '''Test that adding a key/value to your hashtable results in the value being in the data structure'''
    ht = Hashtable()
    idx = ht.hash('dog')
    ht.add('dog','what ever you want')
    ll = ht.buckets[idx]
    key = ll.head.value.get('key')
    value = ll.head.value.get('value')
    assert 'dog' == key
    assert 'what ever you want' == value


def test_hash_get(): ## test 2
    '''Retrieving based on a key returns the value stored'''
    ht = Hashtable()
    ht.add('dog','what ever you want')
    actual = ht.get('dog')
    assert actual == 'what ever you want'

def test_return_none(): ## test 3
    '''Successfully returns None/Null for a key that does not exist in the hashtable'''
    ht = Hashtable()
    ht.add('dog','what ever you want')
    assert ht.contains('dog') == True
    assert ht.contains('cat') == None

def test_hash_handles_collisions(): ## test 4
    '''Test that key collisions are handled properly.'''
    ht = Hashtable()
    ht.add('dog', 'what ever you want')
    ht.add('god', 'not what ever you want')
    actual = ht.get('dog')
    assert actual == 'what ever you want'
    actual = ht.get('god')
    assert actual == 'not what ever you want'

def test_hash(): ## test 6
    '''Successfully hash a key to an in-range value'''

    ht = Hashtable()
    hash_val = ht.hash('apple')
    assert hash_val == 30
    assert ht.hash('apple') == hash_val