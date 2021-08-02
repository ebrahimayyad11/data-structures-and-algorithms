from graph import __version__
from graph.graph import Graph
import pytest

def test_version():
    assert __version__ == '0.1.0'



def test_add_node():
    
    graph = Graph()

    expected = 'ebrahim' 

    actual = graph.add_node('ebrahim').value

    assert actual == expected


def test_add_edge():
    
    graph = Graph()
    start = graph.add_node('start')
    end = graph.add_node('end')
    graph.add_edge(start,end)
    actual = graph.get_neighbors(start)
    excepted = ['end']
    assert actual == excepted




def test_get_nodes():

    graph = Graph()

    graph.add_node('meat')

    graph.add_node('chicken')

    graph.add_node('tomato')

    expected = ['meat','chicken','tomato']

    actual = graph.get_nodes()
    
    assert actual == expected




def test_get_neighbors():

    graph = Graph()

    meat = graph.add_node('meat')
    chicken = graph.add_node('chicken')

    graph.add_edge(meat, chicken)

    expected = ['chicken']
    actual = graph.get_neighbors(meat)

    assert actual == expected



def test_size():

    graph = Graph()

    graph.add_node('osama')

    expected = 1

    actual = graph.size()

    assert actual == expected




def test_one_node_and_one_edge():
    graph = Graph()

    start = graph.add_node('start')
    graph.add_edge(start, start, 10)

    assert graph.size() == 1


def test_size_empty(): 

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected


def test_breadth_first(graphs):
    expected=['b', 'c', 'f', 'a', 'e', 'd']
    actual=graphs[0].breadth_first(graphs[1])
    assert actual == expected 




@pytest.fixture
def graphs():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    graph.add_edge(a, c)
    graph.add_edge(a, d)
    graph.add_edge(b, c)
    graph.add_edge(b, f)
    graph.add_edge(c, a)
    graph.add_edge(c, b)
    graph.add_edge(c, e)
    graph.add_edge(d, a)
    graph.add_edge(d, e)
    graph.add_edge(e, c)
    graph.add_edge(e, d)
    graph.add_edge(e, f)
    graph.add_edge(f, b)
    graph.add_edge(f, e) 

    return graph, b