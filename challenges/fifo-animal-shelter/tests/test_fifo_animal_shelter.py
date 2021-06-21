from fifo_animal_shelter import __version__
from fifo_animal_shelter.fifo_animal_shelter import AnimalShelter


def test_version():
    assert __version__ == '0.1.0'


def test_enqueue():
    actual = []
    animal = AnimalShelter()
    animal.enqueue('zara','dog')
    actual += [animal.dog.peek()]
    animal.enqueue('absi','cat')
    actual += [animal.cat.peek()]
    excepted = ['zara','absi']
    assert actual == excepted


def test_enqueue_fail():
    animal = AnimalShelter()
    actual = animal.enqueue('lolo','horse')
    excepted = 'you can just choose dog or cat'
    assert actual == excepted


def test_dequeue():
    animal = AnimalShelter()
    animal.enqueue('zara','dog')
    animal.enqueue('absi','cat')
    actual = [animal.dequeue('dog'),animal.dequeue('cat')]
    excepted = ['zara','absi']
    assert actual == excepted


def test_dequeue_fail():
    animal = AnimalShelter()
    actual = [animal.dequeue('horse'),animal.dequeue()]
    excepted = ['you can just choose dog or cat','enter the type of the animal']
    assert actual == excepted