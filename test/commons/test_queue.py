from typing import Any

import pytest

from commons.exceptions import NoSuchElementException
from commons.queue import Queue

add_test = [
    (Queue(1, 2, 3, 4, 5, 6), 7, Queue(1, 2, 3, 4, 5, 6, 7)),
    (Queue('u', 'n', 'i', 't'), 'y', Queue('u', 'n', 'i', 't', 'y')),
    (Queue(), 100, Queue(100))
]

peek_test = [
    (Queue(1, 2, 3, 4, 5, 6), 1),
    (Queue('veritasiam', 'smarter everyday'), 'veritasiam')
]

size_test = [
    (Queue(1, 2, 3, 4, 5, 6), 6),
    (Queue('veritasiam', 'smarter everyday'), 2),
    (Queue(), 0)
]

remove_tests = [
    (Queue(1, 2, 3, 4, 5, 6), Queue(2, 3, 4, 5, 6)),
    (Queue('veritasiam', 'smarter everyday', '3blue1brown'), Queue('smarter everyday', '3blue1brown')),
    (Queue('v'), Queue())
]

empty_test = [
    (Queue(), True),
    (Queue('t', 'e', 's', 't'), False)
]


class TestQueue:

    @pytest.mark.parametrize('test_queue, item, expected_queue', add_test)
    def test_add(self, test_queue: Queue, item: Any, expected_queue: Queue):
        test_queue.add(item)
        assert test_queue == expected_queue

    @pytest.mark.parametrize('test_queue, peek_item', peek_test)
    def test_peek(self, test_queue: Queue, peek_item: Any):
        assert test_queue.peek() == peek_item

    def test_peek_emptyqueue(self):
        queue = Queue()
        with pytest.raises(NoSuchElementException):
            queue.peek()

    @pytest.mark.parametrize('test_queue, expected_size', size_test)
    def test_size(self, test_queue: Queue, expected_size: int):
        assert test_queue.size() == expected_size

    @pytest.mark.parametrize('test_queue, expected_queue', remove_tests)
    def test_remove(self, test_queue: Queue, expected_queue: Queue):
        top_elem = test_queue.peek()
        removed_item = test_queue.remove()
        assert removed_item == top_elem and test_queue == expected_queue

    def test_remove_emptyqueue(self):
        queue = Queue()
        with pytest.raises(NoSuchElementException):
            queue.remove()

    @pytest.mark.parametrize('test_queue, isempty', empty_test)
    def test_isempty(self, test_queue: Queue, isempty: bool):
        assert test_queue.isempty() is isempty
