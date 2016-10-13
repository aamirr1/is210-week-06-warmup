#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 6 Warpup task 5"""


def flip_keys(to_flip):
    """This function will reverse the order of the list.
    Args:
        to_flip (list): This is a list for reserve.
    Returns:
        list: a list that the inner sequence has been reversed.
    Examples:
        >>> LIST = [(1, 2, 3), 'abc']
        >>> NEW = flip_keys(LIST)
        >>> LIST is NEW
        True
        >>> print LIST
        [(3, 2, 1), 'cba']
    """
    counter = 0
    for item in to_flip:
        item = to_flip[counter][::-1]
        to_flip[counter] = item
        counter += 1

    return to_flip
