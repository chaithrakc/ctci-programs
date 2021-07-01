import pytest

from ctci.commons.linked_list import LinkedList
from test.test_utils.util import equal

find_tests = [
    (LinkedList(98, 100, 65, 79, 345), 345, 4),
    (LinkedList('m', 'a', 'i', 'l', 'i', 'g'), 'm', 0),
    (LinkedList('partly', 'cloudy', 'raining', 'gloomy', 'weather'), 'raining', 2),
    (LinkedList(), 34, -1),
    (LinkedList(0.98, 0.0002, 56.89), 0.00002, -1)
]

length_tests = [
    (LinkedList(1, 2, 3, 4, 5, 6), 6),
    (LinkedList('test_str'), 1),
    (LinkedList(), 0),
    (LinkedList(56, 89, 100), 3),
    (LinkedList('c', 's', 'u', 'n', 'n', 'y'), 6)
]

clear_test = [
    (LinkedList(1, 2, 3, 4, 5, 6)),
    (LinkedList('test_str')),
    (LinkedList()),
    (LinkedList(56, 89, 100)),
    (LinkedList('c', 's', 'u', 'n', 'n', 'y'))
]

append_tests = [
    (LinkedList(98, 100, 65, 79, 345), [98, 100, 65, 79, 345], 150),
    (LinkedList('m', 'a', 'i', 'l', 'i', 'g'), ['m', 'a', 'i', 'l', 'i', 'g'], 'e'),
    (LinkedList('partly', 'cloudy', 'raining', 'gloomy', 'weather'),
     ['partly', 'cloudy', 'raining', 'gloomy', 'weather'], 'climate'),
    (LinkedList(), [], 34),
    (LinkedList(0.98, 0.0002, 56.89), [0.98, 0.0002, 56.89], 0.00002)
]

insert_tests = [
    # array, index, data_to_insert, expected_list
    (LinkedList(63, 63, 96, 300, 89), 0, 1000, LinkedList(1000, 63, 63, 96, 300, 89)),
    (LinkedList(), 0, 890, LinkedList(890)),
    (LinkedList('N', 'E', 'W', 'Y', 'O', 'R', 'K', 'C', 'I', 'T', 'Y'), 10, 'S',
     LinkedList('N', 'E', 'W', 'Y', 'O', 'R', 'K', 'C', 'I', 'T', 'S', 'Y')),
    (LinkedList('partick', 'jane', 'lisbon'), 2, 'teresa', LinkedList('partick', 'jane', 'teresa', 'lisbon')),
    (LinkedList(150.789), 50, 56.89, LinkedList(150.789, 56.89))
]

remove_tests = [
    # test_array, key_elem, removed_index, expected_array
    (LinkedList(98, 100, 65, 79, 345), 345, 4, LinkedList(98, 100, 65, 79)),
    (LinkedList('m', 'a', 'i', 'l', 'i', 'g'), 'm', 0, LinkedList('a', 'i', 'l', 'i', 'g')),
    (LinkedList('partly', 'cloudy', 'raining', 'gloomy', 'weather'), 'raining', 2,
     LinkedList('partly', 'cloudy', 'gloomy', 'weather')),
    (LinkedList(), 34, -1, LinkedList()),
    (LinkedList(0.98, 0.0002, 56.89), 0.00002, -1, LinkedList(0.98, 0.0002, 56.89))
]

remove_index_tests = [
    # array, remove_index, expected_array
    (LinkedList(63, 63, 96, 300, 89), 0, LinkedList(63, 96, 300, 89)),
    (LinkedList(), 5, LinkedList()),
    (LinkedList('N', 'E', 'W', 'Y', 'O', 'R', 'K', 'C', 'I', 'T', 'Y'), 10,
     LinkedList('N', 'E', 'W', 'Y', 'O', 'R', 'K', 'C', 'I', 'T')),
    (LinkedList('partick', 'lisbon', 'jane'), 1, LinkedList('partick', 'jane')),
    (LinkedList(150.789), 50, LinkedList(150.789))
]

remove_head_tests = [
    (LinkedList(1, 2, 3, 4, 5, 6), LinkedList(2, 3, 4, 5, 6)),
    (LinkedList('test_str'), LinkedList()),
    (LinkedList(), LinkedList()),
    (LinkedList(56, 89, 100), LinkedList(89, 100)),
    (LinkedList('c', 's', 'u', 'n', 'n', 'y'), LinkedList('s', 'u', 'n', 'n', 'y'))
]

remove_tail_tests = [
    (LinkedList(1, 2, 3, 4, 5, 6), [1, 2, 3, 4, 5, 6]),
    (LinkedList('test_str'), ['test_str']),
    (LinkedList(), []),
    (LinkedList(56, 89, 100), [56, 89, 100]),
    (LinkedList('c', 's', 'u', 'n', 'n', 'y'), ['c', 's', 'u', 'n', 'n', 'y'])
]


class TestLinkedList:

    @pytest.mark.parametrize('test_list', clear_test)
    def test_clear(self, test_list):
        test_list.clear()
        assert test_list.head is None

    @pytest.mark.parametrize('test_list, length', length_tests)
    def test_len(self, test_list, length):
        assert test_list.len() == length

    @pytest.mark.parametrize('test_list, key_elem, expected_index', find_tests)
    def test_find(self, test_list, key_elem, expected_index):
        list_index = test_list.find(key_elem)
        assert list_index == expected_index

    @pytest.mark.parametrize('test_list, test_array', remove_tail_tests)
    def test_remove_tail(self, test_list, test_array):
        removed_elem = test_list.remove_tail()
        expected = test_array[len(test_array) - 1] if len(test_array) > 0 else None
        assert removed_elem == expected and equal(test_list, test_array[:-1])

    @pytest.mark.parametrize('test_list, expected_list', remove_head_tests)
    def test_remove_head(self, test_list, expected_list):
        first_elem = test_list.head.data if test_list.head is not None else None
        removed_elem = test_list.remove_head()
        assert removed_elem == first_elem and test_list == expected_list

    @pytest.mark.parametrize('test_list, key_elem, removed_index, expected_list', remove_tests)
    def test_remove(self, test_list, key_elem, removed_index, expected_list):
        list_index = test_list.remove(key_elem)
        assert list_index == removed_index and test_list == expected_list

    @pytest.mark.parametrize('test_list, index, elem, expected_list', insert_tests)
    def test_insert(self, test_list, index, elem, expected_list):
        test_list.insert(index, elem)
        assert test_list == expected_list

    @pytest.mark.parametrize('test_list, test_array, elem', append_tests)
    def test_append_head(self, test_list, test_array, elem):
        test_list.append_head(elem)
        test_array.insert(0, elem)
        assert equal(test_list, test_array)

    @pytest.mark.parametrize('test_list, test_array, elem', append_tests)
    def test_append_tail(self, test_list, test_array, elem):
        test_list.append_tail(elem)
        test_array.append(elem)
        assert equal(test_list, test_array)

    def test_insert_invalid_index(self):
        empty_list = LinkedList()
        index = -5
        with pytest.raises(IndexError) as exc:
            empty_list.insert(index, 'you')
        assert 'Index out of bound:' + str(index) == str(exc.value)

    @pytest.mark.parametrize('test_list, remove_index, expected_list', remove_index_tests)
    def test_remove_index(self, test_list, remove_index, expected_list):
        test_list.remove_index(remove_index)
        assert test_list == expected_list

    def test_remove_invalid_index(self):
        empty_list = LinkedList()
        index = -5
        with pytest.raises(IndexError) as exc:
            empty_list.remove_index(index)
        assert 'Index out of bound:' + str(index) == str(exc.value)
