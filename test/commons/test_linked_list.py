from unittest import TestCase

import pytest

from ctci.commons.linked_list import Node, LinkedList
from test.test_utils.util import equal, get_linkedlist


def get_test_remove():
    return [
        ([98, 100, 65, 79, 345], 345, 4, [98, 100, 65, 79]),
        (['m', 'a', 'i', 'l', 'i', 'g'], 'm', 0, ['a', 'i', 'l', 'i', 'g']),
        (['partly', 'cloudy', 'raining', 'gloomy', 'weather'], 'raining', 2, ['partly', 'cloudy', 'gloomy', 'weather']),
        ([], 34, -1, []),
        ([0.98, 0.0002, 56.89], 0.00002, -1, [0.98, 0.0002, 56.89])
    ]


def get_test_find():
    return [
        ([98, 100, 65, 79, 345], 345, 4),
        (['m', 'a', 'i', 'l', 'i', 'g'], 'm', 0),
        (['partly', 'cloudy', 'raining', 'gloomy', 'weather'], 'raining', 2),
        ([], 34, -1),
        ([0.98, 0.0002, 56.89], 0.00002, -1)
    ]


def get_test_arrays():
    return [
        ([1, 2, 3, 4, 5, 6]),
        (['test_str']),
        ([]),
        ([56, 89, 100]),
        (['c', 's', 'u', 'n', 'n', 'y'])
    ]


def get_testcases_append():
    return [
        ([98, 100, 65, 79, 345], 150),
        (['m', 'a', 'i', 'l', 'i', 'g'], 'e'),
        (['partly', 'cloudy', 'raining', 'gloomy', 'weather'], 'climate'),
        ([], 34),
        ([0.98, 0.0002, 56.89], 0.00002)
    ]


def get_testcases_insert():
    return [
        # array, index, data_to_insert
        ([63, 63, 96, 300, 89], 0, 1000),
        ([], 0, 890),
        (['N', 'E', 'W', 'Y', 'O', 'R', 'K', 'C', 'I', 'T', 'Y'], 10, 'S'),
        (['partick', 'jane', 'lisbon'], 2, 'teresa'),
        ([150.789], 50, 56.89)
    ]


class TestLinkedList:

    @pytest.mark.parametrize('test_array', get_test_arrays())
    def test_clear(self, test_array):
        linked_list = get_linkedlist(test_array)
        linked_list.clear()
        assert linked_list.head is None

    @pytest.mark.parametrize('test_array', get_test_arrays())
    def test_len(self, test_array):
        linked_list = get_linkedlist(test_array)
        assert linked_list.len() == len(test_array)

    @pytest.mark.parametrize('test_array, key_elem, array_index', get_test_find())
    def test_find(self, test_array, key_elem, array_index):
        linked_list = get_linkedlist(test_array)
        list_index = linked_list.find(key_elem)
        assert list_index == array_index

    @pytest.mark.parametrize('test_array', get_test_arrays())
    def test_remove_tail(self, test_array):
        linked_list = get_linkedlist(test_array)
        removed_elem = linked_list.remove_tail()
        expected = test_array[len(test_array) - 1] if len(test_array) > 0 else None
        assert removed_elem == expected and equal(linked_list, test_array[:-1])

    @pytest.mark.parametrize('test_array', get_test_arrays())
    def test_remove_head(self, test_array):
        linked_list = get_linkedlist(test_array)
        removed_elem = linked_list.remove_head()
        expected = test_array[0] if len(test_array) > 0 else None
        assert removed_elem == expected and equal(linked_list, test_array[1:])

    @pytest.mark.parametrize('test_array, key_elem, array_index, expected_array', get_test_remove())
    def test_remove(self, test_array, key_elem, array_index, expected_array):
        linked_list = get_linkedlist(test_array)
        list_index = linked_list.remove(key_elem)
        assert list_index == array_index and equal(linked_list, expected_array)

    @pytest.mark.parametrize('array, index, elem', get_testcases_insert())
    def test_insert(self, array, index, elem):
        linked_list = get_linkedlist(array)
        linked_list.insert(index, elem)
        array.insert(index, elem)
        assert equal(linked_list, array)

    @pytest.mark.parametrize('array, elem', get_testcases_append())
    def test_append_head(self, array, elem):
        linked_list = get_linkedlist(array)
        linked_list.append_head(elem)
        array.insert(0, elem)
        assert equal(linked_list, array)

    @pytest.mark.parametrize('array, elem', get_testcases_append())
    def test_append_tail(self, array, elem):
        linked_list = get_linkedlist(array)
        linked_list.append_tail(elem)
        array.append(elem)
        assert equal(linked_list, array)

    def test_insert_invalid_index(self):
        linked_list = get_linkedlist([])
        index = -5
        with pytest.raises(IndexError) as exc:
            linked_list.insert(index, 'you')
        assert 'Index out of bound:' + str(index) == str(exc.value)
