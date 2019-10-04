# -*- coding: utf-8 -*-

__author__ = 'Ivan Cherednikov'
__email__ = 'ivch@nmbu.no'

import pytest


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sdata = sorted(data)
    n = len(sdata)
    if not sdata != []:
        raise ValueError  # Modifying original code for ValueError test
    return (sdata[n // 2] if n % 2 == 1
            else 0.5 * (sdata[n // 2 - 1] + sdata[n // 2]))


def test_median_single():
    one_element = [6]
    assert median(one_element) == 6


def test_several_lists():
    odd_list = [6, 2, 3, 7, 11]
    even_list = [1, 15, 43, 3]
    order_list = [5, 6, 8, 9]
    revers_list = [10, 9, 5, 2]
    assert median(odd_list) == 6
    assert median(even_list) == 9
    assert median(order_list) == 7
    assert median(revers_list) == 7


def test_for_value_error():
    empty_list = []
    with pytest.raises(ValueError):
        median(empty_list)


def test_original_content():
    original_content = [10, 8, 6]
    new_original_content = original_content
    median(new_original_content)
    assert id(new_original_content) == id(original_content)


def test_median_tuple():
    a_tuple = (10, 2, 15)
    assert median(a_tuple) == 10
