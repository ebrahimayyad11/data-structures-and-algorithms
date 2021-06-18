from stack_and_queue import __version__
from stack_and_queue.stack_and_queue import Stack,Queue


def test_version():
    assert __version__ == '0.1.0'


def test_push():
    st = Stack()
    actual = st.push(4)
    excepted = 4
    assert actual == excepted



def test_push_multiple():
    st = Stack()
    actual = [st.push(4),st.push(2),st.push(3),st.push(5)]
    excepted = [4,2,3,5]
    assert actual == excepted


def test_pop():
    st = Stack()
    st.push(8)
    st.push(5)
    st.push(2)
    actual = st.pop()
    excepted = 2
    assert actual == excepted


def test_multiple_pop():
    st = Stack()
    st.push(5)
    st.push(6)
    st.push(7)
    actual = [st.pop(),st.pop(),st.pop(),st.pop()]
    excepted = [7,6,5,'The Stack is empty!']
    assert actual == excepted



def test_peek_next():
    st = Stack()
    st.push(5)
    st.push(6)
    actual = st.top.next.value
    excepted = 5
    assert actual == excepted



def test_instantiate_empty_stack():
    st = Stack()
    actual = st.isEmpty()
    excepted = True
    assert actual == excepted



def test_call_pop_peek_empty():
    st = Stack()
    actual = [st.pop(),st.peek()]
    excepted = ['The Stack is empty!','The Stack is empty!']




def test_enqueue():
    q = Queue()
    actual = q.enqueue(5)
    excepted = 5
    assert actual == excepted




def test_enqueue_multiple():
    q = Queue()
    actual = [q.enqueue(4),q.enqueue(2),q.enqueue(3),q.enqueue(5)]
    excepted = [4,2,3,5]
    assert actual == excepted


def test_dequeue():
    q = Queue()
    q.enqueue(5)
    q.enqueue(6)
    actual = q.dequeue()
    excepted = 5
    assert actual == excepted


def test_queue_peek():
    q = Queue()
    q.enqueue(5)
    q.enqueue(6)
    actual = q.peek()
    excepted = 5
    assert actual == excepted


def test_multiple_enqueue():
    q = Queue()
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    actual = [q.dequeue(),q.dequeue(),q.dequeue(),q.dequeue()]
    excepted = [5,6,7,'The Queue is empty!']


def test_instantiate_empty_queue():
    q = Queue()
    actual = q.isEmpty()
    excepted = True
    assert actual == excepted



def test_peek_dequeue_empty():
    q = Queue()
    actual = [q.dequeue(),q.peek()]
    excepted = ['The Queue is empty!','The Queue is empty!']
