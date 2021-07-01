import pytest

from test.test_utils.util import equal, get_linkedlist

find_tests = [
    ([98, 100, 65, 79, 345], 345, 4),
    (['m', 'a', 'i', 'l', 'i', 'g'], 'm', 0),
    (['partly', 'cloudy', 'raining', 'gloomy', 'weather'], 'raining', 2),
    ([], 34, -1),
    ([0.98, 0.0002, 56.89], 0.00002, -1)
]

test_arrays = [
    ([1, 2, 3, 4, 5, 6]),
    (['test_str']),
    ([]),
    ([56, 89, 100]),
    (['c', 's', 'u', 'n', 'n', 'y'])
]

append_tests = [
    ([98, 100, 65, 79, 345], 150),
    (['m', 'a', 'i', 'l', 'i', 'g'], 'e'),
    (['partly', 'cloudy', 'raining', 'gloomy', 'weather'], 'climate'),
    ([], 34),
    ([0.98, 0.0002, 56.89], 0.00002)
]

insert_tests = [
    # array, index, data_to_insert
    ([63, 63, 96, 300, 89], 0, 1000),
    ([], 0, 890),
    (['N', 'E', 'W', 'Y', 'O', 'R', 'K', 'C', 'I', 'T', 'Y'], 10, 'S'),
    (['partick', 'jane', 'lisbon'], 2, 'teresa'),
    ([150.789], 50, 56.89)
]

remove_tests = [
    # test_array, key_elem, removed_index, expected_array
    ([98, 100, 65, 79, 345], 345, 4, [98, 100, 65, 79]),
    (['m', 'a', 'i', 'l', 'i', 'g'], 'm', 0, ['a', 'i', 'l', 'i', 'g']),
    (['partly', 'cloudy', 'raining', 'gloomy', 'weather'], 'raining', 2, ['partly', 'cloudy', 'gloomy', 'weather']),
    ([], 34, -1, []),
    ([0.98, 0.0002, 56.89], 0.00002, -1, [0.98, 0.0002, 56.89])
]

remove_index_tests = [
    # array, remove_index, expected_array
    ([63, 63, 96, 300, 89], 0, [63, 96, 300, 89]),
    ([], 5, []),
    (['N', 'E', 'W', 'Y', 'O', 'R', 'K', 'C', 'I', 'T', 'Y'], 10, ['N', 'E', 'W', 'Y', 'O', 'R', 'K', 'C', 'I', 'T']),
    (['partick', 'lisbon', 'jane'], 1, ['partick', 'jane']),
    ([150.789], 50, [150.789]),
]


class TestLinkedList:

    @pytest.mark.parametrize('test_list', test_arrays)
    def test_clear(self, test_list):
        linked_list = get_linkedlist(test_list)
        linked_list.clear()
        assert linked_list.head is None

    @pytest.mark.parametrize('test_list', test_arrays)
    def test_len(self, test_list):
        linked_list = get_linkedlist(test_list)
        assert linked_list.len() == len(test_list)

    @pytest.mark.parametrize('test_list, key_elem, expected_index', find_tests)
    def test_find(self, test_list, key_elem, expected_index):
        linked_list = get_linkedlist(test_list)
        list_index = linked_list.find(key_elem)
        assert list_index == expected_index

    @pytest.mark.parametrize('test_list', test_arrays)
    def test_remove_tail(self, test_list):
        linked_list = get_linkedlist(test_list)
        removed_elem = linked_list.remove_tail()
        expected = test_list[len(test_list) - 1] if len(test_list) > 0 else None
        assert removed_elem == expected and equal(linked_list, test_list[:-1])

    @pytest.mark.parametrize('test_list', test_arrays)
    def test_remove_head(self, test_list):
        linked_list = get_linkedlist(test_list)
        removed_elem = linked_list.remove_head()
        expected = test_list[0] if len(test_list) > 0 else None
        assert removed_elem == expected and equal(linked_list, test_list[1:])

    @pytest.mark.parametrize('test_list, key_elem, removed_index, expected_array', remove_tests)
    def test_remove(self, test_list, key_elem, removed_index, expected_array):
        linked_list = get_linkedlist(test_list)
        list_index = linked_list.remove(key_elem)
        assert list_index == removed_index and equal(linked_list, expected_array)

    @pytest.mark.parametrize('test_list, index, elem', insert_tests)
    def test_insert(self, test_list, index, elem):
        linked_list = get_linkedlist(test_list)
        linked_list.insert(index, elem)
        test_list.insert(index, elem)
        assert equal(linked_list, test_list)

    @pytest.mark.parametrize('test_list, elem', append_tests)
    def test_append_head(self, test_list, elem):
        linked_list = get_linkedlist(test_list)
        linked_list.append_head(elem)
        test_list.insert(0, elem)
        assert equal(linked_list, test_list)

    @pytest.mark.parametrize('test_list, elem', append_tests)
    def test_append_tail(self, test_list, elem):
        linked_list = get_linkedlist(test_list)
        linked_list.append_tail(elem)
        test_list.append(elem)
        assert equal(linked_list, test_list)

    def test_insert_invalid_index(self):
        linked_list = get_linkedlist([])
        index = -5
        with pytest.raises(IndexError) as exc:
            linked_list.insert(index, 'you')
        assert 'Index out of bound:' + str(index) == str(exc.value)

    @pytest.mark.parametrize('test_list, remove_index, expected_list', remove_index_tests)
    def test_remove_index(self, test_list, remove_index, expected_list):
        linkedlist = get_linkedlist(test_list)
        linkedlist.remove_index(remove_index)
        assert equal(linkedlist, expected_list)

    def test_remove_invalid_index(self):
        linked_list = get_linkedlist([])
        index = -5
        with pytest.raises(IndexError) as exc:
            linked_list.remove_index(index)
        assert 'Index out of bound:' + str(index) == str(exc.value)
