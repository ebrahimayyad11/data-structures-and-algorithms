import sys
from typing import Hashable
sys.path.append("/home/ebrahimayyad11/data-structures-and-algorithms/Data-Structures/hash-table")
from hash_table.hash_table import Hashtable

from hashmap_left_join import __version__
from hashmap_left_join.hashmap_left_join import left_join 


def test_version():
    assert __version__ == '0.1.0'


def test1():
    ht1 = Hashtable()
    ht2 = Hashtable()

    ht1.add('fond','enamored')
    ht1.add('wrath','anger')
    ht1.add('diligent','employed')
    ht1.add('outift','garb')
    ht1.add('guide','usher')


    ht2.add('fond','averse')
    ht2.add('wrath','delight')
    ht2.add('diligent','idle')
    ht2.add('guide','follow')
    ht2.add('flow','jam')

    actual = left_join(ht1,ht2)
    excepted = [['diligent', 'employed', 'idle'],
                ['outift', 'garb', None],
                ['fond', 'enamored', 'averse'],
                ['guide', 'usher', 'follow'],
                ['wrath', 'anger', 'delight']
               ]
    assert actual == excepted


def test_first_hashtable_empty():
    ht1 = Hashtable()
    ht2 = Hashtable()

    ht2.add('fond','enamored')
    ht2.add('wrath','anger')
    ht2.add('diligent','employed')
    ht2.add('outift','garb')
    ht2.add('guide','usher')

    actual = left_join(ht1,ht2)
    excepted = 'The first Hashtable is empty'
    assert actual == excepted


def test_second_hashtable_empty():
    ht1 = Hashtable()
    ht2 = Hashtable()

    ht1.add('fond','enamored')
    ht1.add('wrath','anger')
    ht1.add('diligent','employed')
    ht1.add('outift','garb')
    ht1.add('guide','usher')

    actual = left_join(ht1,ht2)
    excepted = [['diligent', 'employed', None],
                ['outift', 'garb', None], 
                ['fond', 'enamored', None], 
                ['guide', 'usher', None], 
                ['wrath', 'anger', None]
               ]
    assert actual == excepted
