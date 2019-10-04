# -*- coding: utf-8 -*-

__author__ = 'Ivan Cherednikov'
__email__ = 'ivch@nmbu.no'


def bubble_sort(input_data):
    nums = len(input_data)
    list_sorted = list(input_data)
    for x in range(nums):
        for z in range(0, nums - x - 1):
            if list_sorted[z] > list_sorted[z + 1]:
                list_sorted[z], list_sorted[z + 1] = (list_sorted[z + 1],
                                                      list_sorted[z])
    return tuple(list_sorted)


def test_empty():
    """Test that the sorting function works for empty list
    """
    an_empty_list = []
    assert bubble_sort(an_empty_list) == ()


def test_single():
    """Test that the sorting function works for single-element list"""
    a_single_element = [18]

    assert bubble_sort(a_single_element) == tuple(a_single_element)


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    """Test that sorting works on sorted data."""

    a_list = [3, 2, 1]
    sorted_list = bubble_sort(a_list)
    assert sorted_list != a_list


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    reverse_sorted = [13, 9, 4, 2]
    sorted_normal = (2, 4, 9, 13)
    assert bubble_sort(reverse_sorted) == sorted_normal


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    identical_element_list = [5, 2, 1, 2, 5]
    identical_sorted = (1, 2, 2, 5, 5)
    assert bubble_sort(identical_element_list) == identical_sorted


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    list_of_lists_and_strings = [[9, 12, 2], [16, 23, 1, 9, 12],
                                 [38, 13, 4, 8],
                                 ['aa', 'bb', 'pp']]

    for ind in range(len(list_of_lists_and_strings)):
        assert bubble_sort(list_of_lists_and_strings[ind]) == \
               tuple(sorted(list_of_lists_and_strings[ind]))
