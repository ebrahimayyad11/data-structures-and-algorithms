from queue_with_stacks import __version__
from queue_with_stacks.queue_with_stacks import PseudoQueue



def test_version():
    assert __version__ == '0.1.0'

def test_enqueue():
    st = PseudoQueue()
    st.enqueue(20)
    st.enqueue(15)
    st.enqueue(10)
    actual = st.enqueue(5)
    excepted = '[5] -> [10] -> [15] -> [20]'  + '\n' + '[5]' 
    assert actual == excepted


def test_dequeue_1():
    st = PseudoQueue()
    st.enqueue(20)
    st.enqueue(15)
    st.enqueue(10)
    st.enqueue(5)
    actual = st.dequeue()
    excepted = 5
    assert actual == excepted


def test_dequeue_2():
    st = PseudoQueue()
    st.enqueue(15)
    st.enqueue(10)
    st.enqueue(5)
    actual = st.dequeue()
    excepted = 10
    assert actual == excepted